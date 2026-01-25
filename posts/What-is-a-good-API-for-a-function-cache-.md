---
layout: post
render_with_liquid: false
date: 2025-12-26
title: "What is a good API for a function cache?"
unlisted: true
---

Ultimately, I just went with
[Joblib](https://joblib.readthedocs.io/en/stable/) instead of rolling my
own solution. Other libraries I looked at:

- <https://github.com/javiber/scrat>
- <https://github.com/python-cachier/cachier>

However, by then I had already written [the
code](https://gist.github.com/mcejp/e77d12751ca2380d50ef7238992c24b9)
and the present write-up, so I decided to publish it anyway.

### Problem statement

I keep running into a problem in my Jupyter notebooks, where some step
of the computation takes just long enough to be annoying whenever it's
necessary to re-run the notebook start to end. It would be great if
these computations could be cached to disk. Without impacting
readability of the notebook, of course.

We're not talking about huge datasets here, by the way. Stuff that
comfortably fits into RAM, let's say tens of megabytes at most.

So what does a good caching API look like? Is it this?

``` python
cache = Cache(BASE_PATH)

if cache.contains(KEY):
    data = cache.get(KEY)
else:
    data = compute()
    cache.put(KEY, data)

use(data)
```

Well, it's certainly a start. But there are some problems. First of all,
what's `KEY`? Can it be a constant string? Not really, if the
computation has any sort of parametrization.

As example, let's take the extraction of an elevation map for a given
region of the world. Let's say it is parametrized by the geographic
extent (min/max latidude and longitude) plus the name of the underlying
dataset from which we want to extract (examples of such datasets with
worldwide coverage are *SRTMGL1* and *NASADEM*). Iterating on the
previous code:

``` python
EXTENT = (51.8, 4.15, 52.2, 4.65)
SOURCE = "SRTM"

cache = Cache(BASE_PATH)

if cache.contains(KEY):
    data = cache.get(KEY)
else:
    data = extract_elevation(EXTENT, SOURCE)
    cache.put(KEY, data)

use(data)
```

### Key generation

Back to `KEY` -- clearly, if any of the parameters change, the
computation needs to be redone. Here's one ad-hoc way to generate the
key:

``` python
EXTENT = (51.8, 4.15, 52.2, 4.65)
SOURCE = "SRTM"

cache = Cache(BASE_PATH)
key = f"elevation_{EXTENT}_{SOURCE}"

if cache.contains(key):
    data = cache.get(key)
else:
    data = extract_elevation(EXTENT, SOURCE)
    cache.put(key, data)

use(data)
```

This will do the job for any strigify-able arguments, but the key length
can get quickly out of hand. It would be preferable to have a
fixed-length key, i.e. a hash. (Also, it's annoying that the key needs
to be passed in multiple places; we'll return to that later)

Let's introduce a little helper function:

``` python
def make_key(*args):
    the_hash = hash(args)
    return f"{the_hash:x}"

# Usage:
key = make_key("elevation", EXTENT, SOURCE)
```

Now we can just throw all the inputs into the argument list and not
worry about the key length exploding (or containing problematic
characters in case it is used directly as a file name)

### Context manager

It is annoying that the key needs to be repeated. What about wrapping it
together with the cache handle in a context manager:

``` python
class CacheEntry:
    def __init__(self, cache, key):
        self._cache = cache
        self._key = key
        self._have_data = key in cache

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass

    def has_data(self):
        return self._have_data

    def get(self):
        return self._cache.get(self._key)

    def put(self, data):
        self._cache.put(self._key, data)
        self._have_data = True

# Usage:
with CacheEntry(cache, make_key(
        "elevation", EXTENT, SOURCE)) as c:
    if c.has_data():
        data = c.get()
    else:
        data = extract_elevation(EXTENT, SOURCE)
        c.put(data)

use(data)
```

### Serialization

The final question to address is that of serialization. If our data is
string or bytes, it's trivial. However, that's rarely the case. Usually
we're dealing with sets of objects, Numpy arrays etc.

With the improvements done so far, working code could look like this:

``` python
EXTENT = (51.8, 4.15, 52.2, 4.65)
SOURCE = "SRTM"

cache = Cache(BASE_PATH)

with CacheEntry(cache, make_key(
        "elevation", EXTENT, SOURCE)) as c:
    if c.has_data():
        data = pickle.loads(c.get())
    else:
        data = extract_elevation(EXTENT, SOURCE)
        c.put(pickle.dumps(data))

use(data)
```

Not terrible, but it could be improved by factoring out the
(de)serialization logic, so it does not need to be repeated in two
places.

We can extend `CacheEntry` to handle serialization internally:

``` python
EXTENT = (51.8, 4.15, 52.2, 4.65)
SOURCE = "SRTM"

cache = Cache(BASE_PATH)

with CacheEntry(cache, make_key(
        "elevation", EXTENT, SOURCE),
        type="pickle") as c:
    if c.has_data():
        data = c.get()
    else:
        data = extract_elevation(EXTENT, SOURCE)
        c.put(data)

use(data)
```
