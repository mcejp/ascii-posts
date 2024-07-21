---
layout: post
render_with_liquid: false
date: 2024-07-19
title: Node-based programming
unlisted: true
---

Advantages:

- up to a certain complexity, easier to skim or to follow data flow due
  to being 2D instead of 1D like code
- for visual data, can see preview at different stages

Problems of graph approach:

- litegraph has issues, would have to maintain own fork
- probably bound to get messy with complexity, as seen in Houdini WFC
  video
- some stuff is ugly from the start (arithmetics)
- not diff-able
- more difficult to use existing library code
- more difficult to compose/reuse graphs (lack of tooling)
- prone to trigger OCD if layout is left to user
