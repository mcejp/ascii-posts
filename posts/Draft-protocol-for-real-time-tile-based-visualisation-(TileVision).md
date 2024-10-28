---
layout: post
render_with_liquid: false
date: 2024-10-24
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

## Food for thought: JSON diff for streaming?

prior art:

- <https://github.com/trailofbits/graphtage?tab=readme-ov-file>
- <https://json-delta.readthedocs.io/en/latest/>
- <https://datatracker.ietf.org/doc/html/rfc6902>
- <https://github.com/ottypes/json1>
