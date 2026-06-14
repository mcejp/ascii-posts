---
layout: post
render_with_liquid: false
date: 2026-06-07
title: "FPGA notes"
unlisted: true
---

### CI

Most recent prior art: [Poly94 GitLab
CI](https://gitlab.com/mcejp/Poly94/-/blob/master/.gitlab-ci.yml)
(related: [Tracking FPGA design build metrics with low infrastructure
footprint](https://mcejp.github.io/2022/06/20/builds.html))

### Register map generators

- Cheby: <https://gitlab.cern.ch/be-cem-edl/common/cheby>
- peakrdl?

### Simulation (and other forms of testing/validation)

- Verilator
- [VUnit](https://vunit.github.io/) (Python)
  - really nice interface, but performance?
- [SVUnit](http://agilesoc.com/open-source-projects/svunit/svunit-getting-started/)
- iverilog: <https://github.com/blazer82/gb.fpga>
- <https://news.ycombinator.com/item?id=23760319> Chisel advocate

**Q: When to use Verilator vs iverilog vs cocotb?** (in Poly94 we use
*all* of them in some way)

#### Verilator

Q: How to build with debugging symbols? A: You can pass
[`--runtime-debug`](https://verilator.org/guide/latest/exe_verilator.html#cmdoption-runtime-debug)
when invoking Verilator. However, it seems to have dramatic impact on
compilation time (depending on the design, of course). If it's too much
and GCC gets stuck for minutes, consider passing just
`-CFLAGS -ggdb -LDFLAGS -ggdb`.

Q: How to create a library instead of an executable? (See this SO
question: <https://stackoverflow.com/q/78452431>)

Q: How to generate a trace (VCD)? A:

1.  `--trace`
2.  `Verilated::traceEverOn(true);`
3.  must implement `double sc_time_stamp()`

### Verilog

Code style: <https://mcejp.gitlab.io/Poly94/code-style.html>

### VCD tooling

- C++ parser: <https://github.com/ben-marshall/verilog-vcd-parser>
- CLI viewer: <https://github.com/yne/vcd>
- Python package: <https://pypi.org/project/Verilog_VCD/> (unmaintained
  since 2016)
  - Github mirror: <https://github.com/zylin/Verilog_VCD>

Q: How to render SVG from VCD? A: One approach is
[vcd2json](https://github.com/nanamake/vcd2json) +
[WaveDromPy](https://github.com/wallento/wavedrompy)
