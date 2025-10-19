---
layout: post
render_with_liquid: false
date: 2025-10-18
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

Communities:

- <https://forum.vcfed.org/index.php?forums/vintage-computer-programming.30/>

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
- Turbo C/C++ & Borland C++
  - [Turbo C++](https://en.wikipedia.org/wiki/Turbo_C%2B%2B) was
    > marketed toward the hobbyist and entry-level compiler market,
    > while [Borland C++](https://en.wikipedia.org/wiki/Borland_C%2B%2B)
    > targeted the professional application development market.

    - Borland C++ 3.1 is the last to support DOS
- Borland Turbo Pascal
- Microsoft Visual C++
- [DataViews](https://news.ycombinator.com/item?id=38794304)
- <https://en.wikipedia.org/wiki/Personal_Editor>

Sound library: <https://github.com/wbcbz7/sndlib-watcom>

### Open Watcom

- docs: <https://www.openwatcom.org/ftp/manuals/current/>; is there
  something better (more browsable & searchable)?

``` c
int32_t mul16x16(int a, int b);

#pragma aux mul16x16 = \
    "imul dx"       \
    parm [dx] [ax] value [dx ax] modify exact [ax dx];
```

#### Detection

<!-- from cguide.pdf -->

Watcom C/C++ compiler: `__WATCOMC__`

CPU:

    16-bit & 32-bit   16-bit     32-bit
    =======================================
    __X86__            __I86__   __386__
    _M_IX86            M_I86     M_I386
                       _M_I86    _M_I386

Note: `_M_IX86` is set equal to n\*100 where n=0 for 8086, 1 for 80186
etc. up to 5 for Pentium.

Target operating system:

    Target          | Macros
    ================|==========================================
    DOS             | __DOS__, _DOS, MSDOS
    OS/2            | __OS2__
    QNX             | __QNX__, __UNIX__
    Netware         | __NETWARE__, __NETWARE_386__
    NT              | __NT__
    Windows         | __WINDOWS__, _WINDOWS, __WINDOWS_386__
    Linux           | __LINUX__, __UNIX__
