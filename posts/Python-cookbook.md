---
layout: post
render_with_liquid: false
date: 2025-10-25
title: "Python cookbook"
unlisted: true
---

### Argument parsing boilerplate

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

### Atomic file update (replace)

Useful for:

- Saving documents to ensure there is always a non-broken version
- git refs operations

APIs:

- Posix: `rename`
- Windows: `ReplaceFile`

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

### Check if an output needs to be rebuilt based on timestamp

``` python
def need_to_rebuild(output_path, source_path):
    try:
        output_mtime = os.path.getmtime(output_path)
    except FileNotFoundError:
        return True

    source_mtime = os.path.getmtime(source_path)

    return output_mtime < source_mtime
```

### Check Python version

``` python
if sys.version_info >= (3, 10):
    print("3.10 or newer")
```

### Format human-readable file size

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

### Join N lists?

    itertools.chain(*list_of_lists)

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

### Print list of dicts as a table (quick-and-dirty)

``` python
def display_table(rows: list[dict]):
    pad = 3
    columns: list[str] = list(rows[0].keys())
    widths = [max(len(col), *(len(row[col] or "") for row in rows)) for col in columns]
    for col, width in zip(columns, widths):
        print(col.ljust(width + pad), end="")
    print()
    for row in rows:
        for col, width in zip(columns, widths):
            print((row[col] or "").ljust(width + pad), end="")
        print()
```

### Random color according to string hash

``` python
def generate_color(s):
    hash_hex = hashlib.md5(s.encode()).hexdigest()
    hue = int(hash_hex[:4], 16) / 0xFFFF
    r, g, b = colorsys.hsv_to_rgb(hue, s=0.5, v=0.65)

    return "#{:02x}{:02x}{:02x}".format(int(r * 255), int(g * 255), int(b * 255))
```
