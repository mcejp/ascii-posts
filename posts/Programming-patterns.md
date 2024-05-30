---
layout: post
render_with_liquid: false
date: 2024-04-07
title: Programming patterns
unlisted: true
---

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
