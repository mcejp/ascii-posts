---
layout: post
render_with_liquid: false
date: 2025-03-14
title: "Embedded filesystems & databases"
unlisted: true
---

### Filesystems

General criteria:

- robustness to power cut (journaling)
- different size of write/erase blocks
- efficiency (footprint, overhead...)

Examples:

- LittleFs looks excellent:
  <https://github.com/littlefs-project/littlefs>

- FatFs <http://elm-chan.org/fsw/ff/00index_e.html>

- eefs: <https://github.com/nasa/eefs> (RTEMS, vxWorks, stand-alone)

- spiffs: <https://github.com/pellepl/spiffs> (in middle of a rewrite as
  of 2023)

- larger: [YAFFS](https://yaffs.net/)

### Databases

- [List](https://github.com/pmwkaa/engine.so)
- <https://github.com/pmwkaa/sophia>: Modern transactional key-value/row
  storage library.
- <https://github.com/symisc/unqlite>: An Embedded NoSQL, Transactional
  Database Engine
- <https://github.com/vmxdev/tkvdb>: Trie key-value database
- <https://github.com/erthink/libmdbx>: One of the fastest embeddable
  key-value ACID database without WAL. libmdbx surpasses the legendary
  LMDB in terms of reliability, features and performance.
- <https://github.com/cruppstahl/upscaledb>: A very fast lightweight
  embedded database engine with a built-in query language.
