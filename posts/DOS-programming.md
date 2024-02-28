---
layout: post
render_with_liquid: false
date: 2024-01-03
title: DOS programming
unlisted: true
---

Compilers:
<https://stackoverflow.com/questions/15096609/c-compiler-for-ms-dos>

GCC for 386: <https://nullprogram.com/blog/2014/12/09/>

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
