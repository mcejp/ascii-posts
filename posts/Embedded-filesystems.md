---
layout: post
render_with_liquid: false
date: 2024-01-03
title: Embedded filesystems
unlisted: true
---

General criteria:

- robustness to power cut (journaling)
- different size of write/erase blocks
- efficiency (footprint, overhead...)

------------------------------------------------------------------------

- LittleFs looks excellent:
  <https://github.com/littlefs-project/littlefs>

- FatFs <http://elm-chan.org/fsw/ff/00index_e.html>

- eefs: <https://github.com/nasa/eefs> (RTEMS, vxWorks, stand-alone)

- spiffs: <https://github.com/pellepl/spiffs> (in middle of a rewrite as
  of 2023)

- larger: [YAFFS](https://yaffs.net/)
