---
layout: post
render_with_liquid: false
date: 2024-04-22
title: Python notes
unlisted: true
---

## Python

### Miscellaneous

#### Check Python version

If we only care about 3.x: `sys.version_info >= (3, 8)`

#### Human-readable file size

- Jinja:
  [filesizeformat](https://jinja.palletsprojects.com/en/3.0.x/templates/#jinja-filters.filesizeformat)

- Generic:

``` python
# From https://stackoverflow.com/a/1094933
def sizeof_fmt(num, suffix="B"):
    for unit in ("", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"):
        if abs(num) < 1024.0:
            return f"{num:3.1f}{unit}{suffix}"
        num /= 1024.0
    return f"{num:.1f}Yi{suffix}"
```

- Alternative: [humanize.naturalsize(bytes, binary:
  bool)](https://stackoverflow.com/a/15485265)

#### How to join N lists?

    itertools.chain(*list_of_lists)

#### Shortcut for `struct.unpack`

``` python
def u(f, format):
    bytes = f.read(struct.calcsize(format))
    return struct.unpack(format, bytes)
```

#### Why not use `set` instead of `list`?

Because `set()` is unordered and iteration order is randomized!

### Argparse boilerplate

``` python
import argparse
form pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument('-a', action='store_true')
parser.add_argument('-b', action='store_true')
parser.add_argument('-c', action='store_true')
parser.add_argument('-i', '--intval', default=4, type=int, help='an int value')
parser.add_argument('-f', default=3.3, type=float, help='a float value')
parser.add_argument('-F', '--file', default='file_that_exists', type=argparse.FileType('w'), help='a filename')
parser.add_argument("positional_arg", help='a string', type=Path)
args = parser.parse_args()
```

### Baseline setup for Python package projects

<https://gist.github.com/mcejp/6b9fbd23028b515399dcf618f2545fe5>

### Building python from source

#### Python 3.10

- Need to install xz-devel to get LZMA

``` bash
./configure --enable-optimizations --enable-loadable-sqlite-extensions --prefix=/opt/python-3.10
make
sudo make altinstall
```

## Jinja

### Jinja boilerplate

``` python
TEMPLATE: str
OUTPUT: Path
MODEL: dict

env = jinja2.Environment(
    loader=jinja2.PackageLoader(__package__),
    # for stand-alone scripts try this:
    #loader=jinja2.FileSystemLoader(Path(__file__).parent),
    # optional
    trim_blocks=True,
    lstrip_blocks=True)

def custom_filter(a: int) -> str:
    return str(a)

env.filters["custom_filter"] = custom_filter

# templates will be searched under <package>/templates/
template = env.get_template(TEMPLATE)

with open(OUTPUT, "wt") as f:
    f.write(template.render(**MODEL))
```

### Template file extension

- [Official
  guidance](https://jinja.palletsprojects.com/en/3.0.x/templates/#template-file-extension)
  is to use either `.jinja` or nothing
- Better to not add it, so as not to break language detection

### Builtin filters reference

<https://jinja.palletsprojects.com/en/3.0.x/templates/#list-of-builtin-filters>

## Logging

### Logging boilerplate

``` python
import logging

logger = logging.getLogger(__name__)

# logger.debug, info, warn, error...
logger.warn("Error: %s", error)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    ...
```

### Structured logging

?

## Matplotlib

### Change markers in middle of scatter

- need to call multiple scatters
- can copy color like this: `color=a._facecolors[0]` (ugh!)
- to not break legend: only specify LABEL for one of the scatter

### Hexagonal plots

<https://stackoverflow.com/a/46526761>

### Legend horizontal (in a row)

Add `ncol=XX`

### Legend outside of axes

Possible but complicated: <https://stackoverflow.com/a/43439132>

### Font size

    matplotlib.rcParams.update({'font.size': 22})

## Numpy

### Chained `logical_and` / `logical_or`

    np.logical_and.reduce((a, b, c, ...))

### Types to use/avoid

Use:

- `np.uint8`, `np.int32` etc.
- `np.float32`, `np.float64`

Avoid:

- `"byte"`
- `np.byte`
- `np.float`

## Pillow

### Palette from raw bytes (RGB888)

``` python
pal = (np.frombuffer(pal_bytes, dtype=np.uint8)
         .reshape((-1, 3)))
```

### Image from raw bytes + palette

``` python
indexes = (np.frombuffer(image_bytes, dtype=np.uint8)
             .reshape((H, W)))
rgb = np.zeros_like(pal, shape=(indexes.shape[0],
                                indexes.shape[1], 3))
np.take(pal, indexes, out=rgb, axis=0)
img = Image.frombytes("RGB", (indexes.shape[1],
                              indexes.shape[0]), rgb)
```
