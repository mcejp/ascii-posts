---
layout: post
render_with_liquid: false
date: 2025-09-29
title: "Programming patterns"
unlisted: true
---

### Cache a computation using Numpy

``` python
try:
    example = np.load("example.npy")
except FileNotFoundError:
    example = compute()
    np.save("example.npy", example)
```

### Cache a computation using Pickle + gzip

``` python
import gzip
import pickle

try:
    with gzip.open("example.pickle.gz", "rb") as f:
        a, b, c = pickle.load(f)
except FileNotFoundError:
    a, b, c = compute()

    with gzip.open("example.pickle.gz", "wb") as f:
        pickle.dump((a, b, c), f)
```

### Check if an output needs to be rebuild from source based on modification timestamp

``` python
def need_to_rebuild(output_path, source_path):
    try:
        output_mtime = os.path.getmtime(output_path)
    except FileNotFoundError:
        return True

    source_mtime = os.path.getmtime(source_path)

    return output_mtime < source_mtime
```
