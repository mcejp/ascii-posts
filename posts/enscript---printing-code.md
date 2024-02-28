---
layout: post
render_with_liquid: false
date: 2024-01-03
title: enscript - printing code
unlisted: true
---

# A4, single column, fancy-header
    enscript -1G \
             --line-numbers \
             --media=A4 \
             --highlight=verilog \
             -o - \
             rtl/Memory_Ctrl.sv \
             | ps2pdf - Memory_Ctrl.pdf
