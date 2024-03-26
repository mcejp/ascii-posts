---
layout: post
render_with_liquid: false
date: 2024-03-26
title: Documenting projects
unlisted: true
---

## General observations

- Projects evolve, so any documentation that cannot be trivially updated
  is doomed to be obsolete
- Your best chance of keeping docs up to date is to make them part of
  the source code -- same as your
  [changelog](https://keepachangelog.com/)
- API docs should be extracted from the source code and incorporated
  within a *human-designed* overall structure.
  [Sphinx](https://www.sphinx-doc.org/) does a good job of enabling
  this.
- It is okay to have some redundancy between different documents when it
  helps readbility or clarifies the context
  - For example, a glossary will most likely contain some information
    that is repeated in main text

## Types of documentation

### User Guide & Developer's Guide

- two different audiences, but very similar process
- should be *aggressively* kept up-to-date
  - version-controlled together with the code
- deployment should be automated, so that it does not require ongoing
  effort (for example, via Github/GitLab Pages)

#### Recommended tool: Sphinx

- natively supports Python API docs
- C/C++ via Breathe extension
- reST language is powerful -- but comes with a learning curve
- high-quality themes available

Drawbacks:

- not interconnected between projects organization-wide, usually no
  global search
- tables in reST are not very good

Examples:

- [CMake documentation](https://cmake.org/cmake/help/latest/)
- [The Linux Kernel documentation](https://docs.kernel.org/)

### Wiki

- excellent for planning and writing down meeting minutes
- less suitable for documenting the product itself

Main strengths:

- global search
- collaborative editing, WYSIWYG
- cross-links between projects less likely to break
- attachments

Drawbacks:

- since it is not part of source code, it's easier to forget to update
  it when implementing a change
- usually very difficult to propagate information from source code on
  push/release
- not always easy to reorganize and move pages around (since they are
  not plain files)
- 'live information' can only be embedded via specific plug-ins (e.g.,
  JIRA)
- if using a proprietary solution: vendor lock-in, difficulty of content
  migration

### Technical report

- written once and usually not updated
- excellent place to discuss *reasoning* behind the decisions made and
  the design process in general (but often these could just be included
  in Developer's Guide)

#### Recommended tool: LaTeX

Strengths:

- mature feature set
  - cross-references
  - powerful tables
  - equations
  - bibliography
- outputs to PDF which is easy to pass around
- Overleaf
- gorgeous typesetting

Drawbacks:

- learning curve
- LaTeX code very difficult to read and maintain

Examples:

- CERN Accelerators & Technology Sector Notes, for example [this
  one](https://cds.cern.ch/record/2647213/files/CERN-ACC-NOTE-2018-0071.pdf)
- [Technical design of the Bmboot
  monitor](https://edms.cern.ch/ui/file/3028102/1/Bmbook-v0.6.pdf)

### Article / blog post

- written once and usually not updated
- good way to present the project to a new audience, or just inform
  about recent progress
- in practice, this is often the only place documenting the architecture
  and internals
  - this is bad -- it will be difficult to find this information later,
    and it might become obsolete

#### Recommended tool: LaTeX (for journal/conference articles)

#### Recommended tool: Jekyll (for blog posts)

## Additional resources

- [CERN English language Style
  Guide](https://translation-council-support-group.web.cern.ch/sites/default/files/styles/CERN%20TM%20English%20language%20style%20guide.pdf)
