---
layout: post
render_with_liquid: false
date: 2024-06-05
title: JIT / recompilation
unlisted: true
---

### JIT libraries

- [Xbyak](https://github.com/herumi/xbyak) looks amazing (x86)
- LLVM: [ORC](https://llvm.org/docs/ORCv2.html)
- GCC: libgccjit
- Might be also useful: libunwind

### IR JITs

- [Cranelift](https://github.com/bytecodealliance/cranelift-jit-demo)
- <http://themaister.net/blog/2019/01/27/an-unusual-recompiler-experiment-mips-to-llvm-ir-part-1/>
- ARM: Citra, Yuzu, EKA2L1 (all the same, for x86_64 & ARM64)
- LuaJIT's DynASM; great writeup: <https://github.com/sysprog21/jitboy>
- PCSX2
  <https://github.com/PCSX2/pcsx2/blob/master/pcsx2/x86/microVU_Compile.inl>
- <https://wiki.mozilla.org/Tamarin:Tracing>
- <https://github.com/pcercuei/lightrec>: MIPS-to-everything dynamic
  recompiler for PSX emulators
- [NanoJIT](https://github.com/dibyendumajumdar/nanojit)? Unmaintained.

### x86_64-\>arm64 dynarec

- <https://github.com/ptitSeb/box64>

### x86-\>wasm

- <https://github.com/copy/v86>

### N64-\>C static recompiler

- <https://github.com/N64Recomp/N64Recomp>
  - Inspired by: <https://github.com/decompals/ido-static-recomp>
