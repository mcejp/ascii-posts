---
layout: post
render_with_liquid: false
date: 2023-06-25
title: Generic data container formats
unlisted: true
---

### HDF5

- Pros:
  - good interop with numpy
  - fast & efficient
- Cons:
  - cannot update atomically -\> probably no good for real-time sim
    - work-around: write a new file every time
- TBD:
  - usability of the C/C++ API
