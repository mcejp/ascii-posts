---
layout: post
render_with_liquid: false
date: 2025-12-26
title: "PDF manipulation"
unlisted: true
---

### Create empty page

    convert xc:none -page A4 portrait.a4.pdf
    convert xc:none -page 842x595 landscape.a4.pdf

### Extract all images from a document ([pdfimages](https://en.wikipedia.org/wiki/Pdfimages))

    mkdir out
    pdfimages -all document.pdf out

### Extract a range of pages

    qpdf thesis.pdf --pages . 31-38 -- extract.pdf

### Merge (concatenate) several PDF files

**Careful to not omit the last argument!**

    pdfunite in-1.pdf in-2.pdf in-n.pdf out.pdf

### Multiple pages per sheet

    pdfjam --a4paper --nup 2x1 in.pdf --outfile out.pdf --landscape

### Plaintext to PDF (for printing)

    pandoc -V geometry:margin=2cm -V papersize:a5 forth.txt -o forth.pdf

### Printing code (enscript)

    # A4, single column, fancy-header
    enscript -1G \
             --line-numbers \
             --media=A4 \
             --highlight=verilog \
             -o - \
             rtl/Memory_Ctrl.sv \
             | ps2pdf - Memory_Ctrl.pdf

### Search (grep) across PDF documents

    sudo dnf install pdfgrep
    pdfgrep pattern *.pdf
