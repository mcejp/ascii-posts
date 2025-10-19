---
layout: post
render_with_liquid: false
date: 2024-04-07
title: "SQL"
unlisted: true
---

- Alphabetic order for fields in SELECT! The only maintainable solution.
- Do not use UNSIGNED; it is non-standard and not all that useful:
  <https://stackoverflow.com/a/4452091>
- MySQL: nullable columns always have a default value of `NULL`
- [Dolt is Git for Data](https://github.com/dolthub/dolt)

### SQL criticism

- [Some opinionated thoughts on SQL databases
  (2021)](https://blog.nelhage.com/post/some-opinionated-sql-takes/)
- [Against SQL
  (2021)](https://scattered-thoughts.net/writing/against-sql/)

### Usage in C++

- [Mapping generator
  (databasetool)](https://github.com/vengi-voxel/vengi-archive/blob/master/docs/Persistence.md)
  ([code](https://github.com/vengi-voxel/vengi-archive/tree/master/src/tools/databasetool))
- Real-world example:
  [ThumbnailDatabase](https://github.com/chromium/chromium/blob/6cd43a16fac2538a44ca46e2e00a3632bbbba8f6/components/history/core/browser/thumbnail_database.cc)
  in Chromium
