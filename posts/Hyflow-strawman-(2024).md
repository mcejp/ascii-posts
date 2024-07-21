---
layout: post
render_with_liquid: false
date: 2024-07-21
title: Hyflow strawman (2024)
unlisted: true
---

## Vision

- keep browser window open (even better: VSCode tab?) focused on a part
  of the DAG with inline preview.
- Upon editing the code, the view is refreshed, keeping the pan/zoom
  position.
- DAG is laid out automatically from user code.
- (automatic/guided parallelization of computation)

Even better: use something like Golden Layout where main pane shows the
DAG but it is possible to open sub-panes with intermediate results or
the 3D view

### Feature wishlist

- set *defaults* for ops (e.g., dimensions for Perlin noise)
- tweakable *parameters*
- *variants* (parameter presets)

## MVP ("Lyra")

- script is just Hy
- provide a package to do the following:
  - collect intermediate visualizations
  - generate HTML page
- use with livereload

#### Q: can embed 3D view on page?

A: this might work:
<https://github.com/google/model-viewer/tree/master/packages/model-viewer>

## (MVP)^2

- just inspect intermediates as PNG in editor
- use [editor plugin to view
  GLB](https://github.com/cloudedcat/vscode-model-viewer)
