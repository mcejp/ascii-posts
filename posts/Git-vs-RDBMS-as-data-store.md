---
layout: post
render_with_liquid: false
date: 2024-04-27
title: "Git vs RDBMS as data store"
unlisted: true
---

Git advantage:

- decentralized, offline
- branching
- easy to diff, to backup, to parse (if suitable language chosen)

Advantage of text files specifically:

- trivial to access
- can have comments
- hierarchical data

Hosted database:

- easy to build GUI (ecosystem there -- much less so for plain files)
- difficult to access
- scales to much larger size
  - indexing -\> faster to search
- transactions

Sqlite:

- in Git: mostly combines disadvatages and makes a mess
- scales pretty well
- doesn't play nice with Dropbox/NFS

Editing non-text files as text: [Example from Pixar
(USDEdit)](https://graphics.pixar.com/usd/release/tut_helloworld.html#viewing-and-editing-usd-file-contents)
