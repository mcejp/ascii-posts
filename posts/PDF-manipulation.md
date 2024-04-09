---
layout: post
render_with_liquid: false
date: 2024-04-09
title: PDF manipulation
unlisted: true
---

Merging PDF, **careful to not omit last argument**:

    pdfunite in-1.pdf in-2.pdf in-n.pdf out.pdf

Multiple pages per sheet

    pdfjam --a4paper --nup 2x1 in.pdf --outfile out.pdf --landscape

Create empty page

    convert xc:none -page A4 portrait.a4.pdf
    convert xc:none -page 842x595 landscape.a4.pdf

Extract pages

    qpdf thesis.pdf --pages . 31-38 -- extract.pdf

Extract all images from a document
([pdfimages](https://en.wikipedia.org/wiki/Pdfimages))

    mkdir out
    pdfimages -all document.pdf out
