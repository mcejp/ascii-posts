---
layout: post
render_with_liquid: false
date: 2024-03-27
title: Libraries
unlisted: true
---

## Native (C/C++)

| description                                | library                                                         |
|--------------------------------------------|-----------------------------------------------------------------|
| Arbitrary precision floating point numbers | <https://bellard.org/libbf/>                                    |
| Audio (minimalist)                         | <https://github.com/mackron/miniaudio>                          |
| Checked (overflow) arithmetic              | <https://github.com/xiw/libo>                                   |
| ECMAScript (tiny)                          | <https://bellard.org/quickjs/>                                  |
| Fast I/O (to be reviewed)                  | <https://github.com/expnkx/fast_io>                             |
| In-process key-value database              | ?                                                               |
| Math expression parsing                    | <https://codeplea.com/tinyexpr>                                 |
| printf                                     | <https://github.com/charlesnicholson/nanoprintf>                |
| Self-backdoor                              | <https://github.com/buserror/libmish>                           |
| Small libc                                 | <https://github.com/managarm/mlibc>                             |
| SQL parser                                 | ? <https://stackoverflow.com/questions/1147212/sql-parser-in-c> |
| Trace-back                                 | ??? (libunwind ?)                                               |

ZeroRPC for RPC ?

## C++

| purpose                              | library                                                              |
|--------------------------------------|----------------------------------------------------------------------|
| Assert                               | [maybe this](https://github.com/stephenmathieson/assertion-macros.h) |
| Bit vector compression               | <https://github.com/lemire/EWAHBoolArray>                            |
| Canvas                               | <https://github.com/a-e-k/canvas_ity>                                |
| Clipboard                            | <https://github.com/dacap/clip>                                      |
| debugbreak                           | <https://github.com/scottt/debugbreak>                               |
| libnativefiledialog                  | or: <https://github.com/samhocevar/portable-file-dialogs.git>        |
| Logging                              | spdlog                                                               |
| Node Editor using ImGui              | <https://github.com/thedmd/imgui-node-editor>                        |
| Observable                           | <https://github.com/dacap/observable>                                |
| Triangulation of polygons            | <https://github.com/ruslashev/poly2tri>                              |
| Triangulation of polygons (not only) | <https://github.com/micro-gl/micro-tess>                             |
| Qt Markdown                          | <https://github.com/pbek/qmarkdowntextedit>                          |
| Qt MVVM                              | <https://github.com/gpospelov/qt-mvvm>                               |
| Serialization                        | <https://github.com/KonanM/tser>                                     |
| SW rendering                         | <https://github.com/Vogtinator/nGL>                                  |
| WebView                              | <https://github.com/webview/webview>                                 |

## Java

| purpose                          | library                                    |
|----------------------------------|--------------------------------------------|
| JetBrains-inspired LAF for Swing | <https://github.com/JFormDesigner/FlatLaf> |

also: FreePlane -- professional-looking Java UI (at least on Win10)
(uses Flat IntelliJ LAF)

## Python

| purpose                  | library                                       |
|--------------------------|-----------------------------------------------|
| C++11-Python interfacing | <https://github.com/pybind/pybind11>          |
| Ninja generator          | <https://github.com/mjansson/ninja_generator> |
| OBJ files                | <https://github.com/mjansson/obj_lib>         |

## ECMAScript

anti-javascript-fatigue javascript framework:
<https://github.com/bigskysoftware/htmx>

## Audio libraries

- pindrop
- soloud

## Malloc alternatives

xalloc, umm_alloc, <https://github.com/mjansson/rpmalloc> (many others)

## Verilog

<https://github.com/Laxer3a/libVerilog> -\> clamping, rounding