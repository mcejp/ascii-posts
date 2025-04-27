---
layout: post
render_with_liquid: false
date: 2024-03-20
title: "LaTeX tips & tricks"
unlisted: true
---

### Alt text for caption (e.g. for TOC)

``` latex
\caption[Alt text]{Full text (\cite{source}) \label{fig:hello-world}}
```

### Batch compilation in scripts, CI etc.

Use `latexmk` instead of calling latex directly

### Bytefield broken (header disappearing)

Instead of specifying a range of bits in the bitheader, enumerate them
one by one

### Bytefield nesting

<https://tex.stackexchange.com/questions/155647/combining-packets-of-different-layers>

### Extract range of pages from PDF

    qpdf thesis.pdf --pages . 11-89 -- output.pdf

But, resultant file seems huge. Can also do Print to PDF.

### Fonts

Catalogue: <https://tug.org/FontCatalogue/seriffonts.html>

Libertine *really nice* (ACM Proceedings)

### Inkscape export -\> EPS or PDF?

[No reason to use EPS. No transparency
support.](https://www.graphicdesignforum.com/t/eps-vs-pdf/7424/3) Both
formats seem to preserve text fine.

### Math

- `$ .. $` vs `\( ... \)` is tough. latter is preferred, but a bit
  unreadable
- do not use `$$ ... $$` (plain TeX syntax)
- do use `\[ ... \]` (for unnumbered)
- do use `\begin{equation}` (for numbered)

### Rendering formulas to PNG

<https://quicklatex.com/>

### Tables that look good

[booktabs](https://nhigham.com/2019/11/19/better-latex-tables-with-booktabs/)

### Two figures side-by-side

<https://tex.stackexchange.com/a/282878>

But captions broken in *ctuthesis* -\> change `estylefloat{figure}` to
`estylefloat*{figure}` in *ctuth-pkg*

### URLs in bibliography

<https://tex.stackexchange.com/questions/186235/in-bibtex-when-should-i-use-howpublished-and-when-url>
