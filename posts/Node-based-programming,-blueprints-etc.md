---
layout: post
render_with_liquid: false
date: 2025-03-14
title: "Node-based programming, blueprints etc."
unlisted: true
---

#### Editors/tools

- litegraph.js
- Blender shaders
- Unreal Blueprints
- Node-RED
- qt plots; custom node editor: <https://www.pyqtgraph.org/>
- Houdini
- Filter Forge

Not investigated yet:

- xyflow
- <https://github.com/leon-thomm/Ryven>
- <https://github.com/wonderworks-software/PyFlow>
- <https://github.com/Bycelium/PyFlow>

#### Advantages

- up to a certain complexity, easier to skim or to follow data flow due
  to being 2D instead of 1D like code
- for visual data, can see preview at different stages

#### Problems of graph approach

- litegraph has issues, would have to maintain own fork
- probably bound to get messy with complexity, as seen in Houdini WFC
  video
- some stuff is ugly from the start (arithmetics)
- not diff-able
- more difficult to use existing library code
- more difficult to compose/reuse graphs (lack of tooling)
- prone to trigger OCD if layout is left to user

#### More thoughts

A big value of schematics is how they can show different levels of
abstraction. A given subset of a system can appear on different sheets
with different degree of zoom-in. Some links can also be omitted if they
are deemed not relevant (for example: in a block diagram of digital
logic you would not show the power supply network)

When a system is *defined* in a node-based language, you have to work
with nodes at a low level of abstraction -- the primitives provided by
the language. Sure, in all but the most limited of tools, you can
introduce sub-blocks, yet they don't solve many of the limitations
stated above. It is a bit better if you can expand sub-blocks "inline"
while editing, so you can simultaneously see subsystem boundaries as
well as the nitty-gritty of the implementation.

By the way, an analogous problem arises when you try to *generate* a
schematic for a design that is not already highly structured. Think
schematics created by logic synthesis tools; they tend to be a mess
navigate (It doesn't help that automatic layouting is pretty tricky).
The only thing stopping them from being entirely useless is the fact
that logic designs are very hierachical in practice.
