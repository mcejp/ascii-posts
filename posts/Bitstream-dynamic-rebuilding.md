---
layout: post
render_with_liquid: false
date: 2024-01-03
title: Bitstream dynamic rebuilding
unlisted: true
---

> Brings back a memory of a company that made Logic Analyzers some 20+
> years ago. They used a fairly simple FPGA (or cpld) back then but
> still managed to put complex triggering algorithms by calculating a
> new bitstream on the fly and uploading the new variant into the FPGA
> each time a trigger setting was changed. This also had better timing
> compared with putting registers in the FPGA and setting bits in those
> registers to change triggering.
>
> I’m not sure what exactly happened, but I think they had to cancel the
> whole product line after that particular FPGA went out of production.
> Using another FPGA with closed bitstream format would have forced them
> to use the “regiser” way, and would have made the product too
> expensive, or the timing to slow. They may have switched to a simpler
> triggering scheme for the “next version” of their Logic Analyzer.
