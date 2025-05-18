---
layout: post
render_with_liquid: false
date: 2025-05-11
title: "DOS programming"
unlisted: true
---

General intro: <https://alexfru.narod.ru/os/c16/c16.html>

Compilers:
<https://stackoverflow.com/questions/15096609/c-compiler-for-ms-dos>

GCC for 386: <https://nullprogram.com/blog/2014/12/09/>

x86 reference:

- <https://faydoc.tripod.com/cpu/index.htm>
- <https://edge.edx.org/c4x/BITSPilani/EEE231/asset/8086_family_Users_Manual_1_.pdf>
  instruction set reference @ 66

DOS reference:

- <http://spike.scu.edu.au/~barry/interrupts.html#ah3c>
- <http://www.o3one.org/hwdocs/bios_doc/dosref22.html>
- <https://github.com/joncampbell123/doslib>

GUI:

- <https://github.com/bluewaysw/pcgeos>
- Turbo Vision: <https://github.com/magiblot/tvision>
- <https://github.com/jharg93/SvgaBGI>

Rust:

- <https://github.com/Serentty/rusty-dos>

Line endings:

- `getch()` will return \r on enter
- but if you pipe in a Linux textfile, obviously you will get \n

IDEs:

- [CLion](https://github.com/open-watcom/open-watcom-v2/issues/596#issuecomment-1200146390)
- Borland Turbo C/C++
- Borland Turbo Pascal
- Microsoft Visual C++
- [DataViews](https://news.ycombinator.com/item?id=38794304)

Open Watcom:

- docs: <https://www.openwatcom.org/ftp/manuals/current/;> is there
  something better (more browsable & searchable)?
