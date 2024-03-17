---
layout: post
render_with_liquid: false
date: 2024-03-15
title: Draft protocol for real-time tile-based visualisation (TileVision)
unlisted: true
---

## General

Communication is carried over WebSocket via text messages -- but in
principle any two-way communication can work if it can transmit lines of
plaintext.

### Coordinate system?

## Command language

### Server --\> Client

These commands are JSON-encoded.

#### HELLO command

``` python
class HelloCommand:
    command = "HELLO"
    w: int          # map width in tiles
    h: int          # map height in tiles
    bg: list[str]   # list of "#rrggbb" strings (w x h elements)
```

#### LABELS command

``` python
class LabelsCommand:
   command = "LABELS"
   labels: list[Label]
   paths: list[Path]

class Label:
   x: float         # in units of ??
   y: float         # in units of ??
   text: str
   color: str
   fontsize: float  # in units of ??

class Path:
   d: str           # SVG path string
                    # (see https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorial/Paths)
   linedash: Optional[list]
   linewidth: Optional[float]
   stroke: Optional[str]
   fill: Optional[str]
```

#### REPORT command

(sent only upon pausing the simulation)

``` python
class ReportCommand:
    command = "REPORT"
    text: str
```

#### STATE command

``` python
class StateCommand:
    command = "STATE"
    paused: bool
```

#### SET-TITLE command

``` python
class SetTitleCommand:
    command = "SET-TITLE"
    title: str
```

### Client --\> Server

These are just plaintext messages for now.

- `PAUSE`
- `STEP`
