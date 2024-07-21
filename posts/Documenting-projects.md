---
layout: post
render_with_liquid: false
date: 2024-04-09
title: Documenting projects
unlisted: true
---

Oh no, documentation... everyone seems to hate writing it, and everyone
seems to hate reading it (because look how poorly it is written, *of
course*). Yet, often it can be the only way to preserve crucial
knowledge for future generations. This effect is particularly pronounced
in organizations like [CERN](https://home.cern/), where many people come
on relatively short fixed-term contracts, and face-to-face knowledge
transfer doesn't always work out.

But documentation is so often misunderstood as a mere vehicle for
information. That couldn't be further from the truth! For one, writing
documentation leads you to explain the reasoning behind your choices,
and thus challenge the implicit assumptions you made along the way (as
any holes in your chain of reasoning will become plainly visible). More
than once have I witnessed someone reach an *Aha!* moment, which caused
them to rethink fundamental assumptions in their approach to a problem,
during the course of "just writing some docs for completeness". How they
wished they had done that earlier!

I believe that there are two keys to breaking the vicious circle of poor
documentation leading to low engagement leading to low investment in
documentation leading to... It starts with acquiring
<span style="font-variant: small-caps">The Right Mindset</span>, which
I'd argue boils down to asking yourself **who** will need **what
information** and **when**, and using this to select the most
appropriate **format** (or, usually, multiple formats).

The second step is to select
<span style="font-variant: small-caps">Tools Which Will Empower
You</span> on your mission, rather than hinder your efforts. In this
post, whose primary purpose is to serve as a cheatsheet to myself, I
attempt to formulate my views on writing docs, and give tips about the
tools that help me every day.

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

This cannot be emphasized enough -- use the right ~~tool~~ format for
the job at hand!

### User guide & Developer's guide

- two different audiences, but very similar process
- should be *aggressively* kept up-to-date
  - version-controlled together with the code
- deployment should be automated, so that it does not require ongoing
  effort (for example, via Github/GitLab Pages)

#### Recommended tool: Sphinx

Advantages:

- natively supports Python API docs
- C/C++ via Breathe extension
- reST language is powerful -- although this power comes with a learning
  curve
- high-quality themes freely available

Drawbacks:

- not interconnected between projects organization-wide, usually no
  global search
- tables in reST are... clunky

Examples:

- [CMake Reference Documentation](https://cmake.org/cmake/help/latest/)
- [The Linux Kernel documentation](https://docs.kernel.org/)

#### Honorable mention: Jekyll

I wouldn't recommend it *for this usecase* because it's less structured
by default, but the systemd project [has done spectacular
work](https://systemd.io/PORTABILITY_AND_STABILITY/) using it ([source
code
here](https://github.com/systemd/systemd/tree/8959e17d736fbdbaf7cd912f35d23ced2e261327/docs))

### Wiki (DokuWiki, Confluence...)

- excellent for planning, writing down meeting minutes, drafting new
  ideas...
- less suitable for documenting the product itself

Advantages:

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
  the design process in general (although these would usually deserve to
  be included in Developer's guide as well)

#### Recommended tool: LaTeX

Advantages:

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

### Talk / Presentation / Lecture

There is a certain warmth to human speech which cannot be replicated in
writing, no matter how skilled. A talk can be inspiring, funny, yet also
strangely comforting and reassuring... It is a great medium for
conveying information that is stable -- otherwise, keeping it up-to-date
can be a challenge.

Strengths:

- uniqueness of the human touch
- can be consumed somewhat passively

Limitations:

- very difficult to keep a recorded talk up-to-date in face of change
- not searchable with current technology, difficult to skim a video

You can find more of my opinions on this topic in [this
post](Making-impactful-presentations.html).

## Figures

In LaTeX, the [TikZ](https://tikz.net/) package is essentially
legendary... but personally, I always got too frustrated trying to use
it (beyond just copying snippets of already working code from SO). My
go-to is [~~draw.io~~ diagrams.net](https://app.diagrams.net/). It's a
remarkable tool, extremely easy to get started, but surprisingly
powerful ever for complex diagrams.

I have also enjoyed using [yEd](https://www.yworks.com/products/yed)
(but I'm never sure about its license terms). Its automatic layout
features are particularly handy for mind-mapping, or exploring design
spaces.

## Additional resources

- [CERN English language Style
  Guide](https://translation-council-support-group.web.cern.ch/sites/default/files/styles/CERN%20TM%20English%20language%20style%20guide.pdf)
- [How writing creates
  value](https://alexkrupp.typepad.com/sensemaking/2010/06/how-writing-creates-value-.html)
- [An online tree-like utility for generating ASCII folder structure
  diagrams](https://tree.nathanfriend.io/)

## Opinions of other people that I might or might not agree with

#### Exhibit A

> #### General Guidance on Technical Writing
>
> While we do not provide specific guidance on writing, in general,
> follow the “four Cs” of technical documentation:
>
> - Complete: the document must completely describe the subject matter
> - Correct: the document must be factually correct
> - Concise: the document must include only what needs to be there
> - Consistent: the document’s content and tone must be uniform within
>   the document itself as well as with other related documents

#### Exhibit B

> Documentation should include:
>
> - Description of what the program/library is supposed to do. What is
>   it expected to be used for.
> - What is the user API, how does one use the the program/library -
>   including tutorials and examples.
> - High level description of implementation strategy
> - What are the design decisions
> - What is the rationale/motivation for these decisions
>
> Documentation should not include:
>
> - Implementation details. These should be in code itself. If the code
>   is not obvious, then either the code should be changed or comments
>   added.
> - Reference to any private implementation details.
>
> **Documentation prepration should be seen as an aid to building a
> coherent design rather than some afterthought** to try and fix
> something that has been made over complicated in the first place.
>
> --
> [reddit.com/r/cpp/](https://www.reddit.com/r/cpp/comments/8lwmkb/which_tool_do_you_use_to_document_your_c_code/dzkde8e/),
> emphasis mine

#### Exhibit C

> I very much despise the trend to write sharepoint or wiki/Confluence
> pages as a means for software documentation. I want my documentation
> to reside next to my source code, not at some obscure corporate URL.

#### Exhibit D

> I find it hard to get people to write down anything. And if they do,
> they often times don't put enough effort into it, like writing down
> some bullet points without context or screenshots without adding text.
> This is a personal and cultural problem at companies and in teams. A
> lot of people don't know how to generate value from taking
> notes/documentation and aren't good writers in general. I'm still
> thinking about how you can teach people what's important when it comes
> to writing and when to take notes.
>
> (...) Search is probably even more important than taking notes in the
> first place. I find myself searching through my notes multiple times a
> day, even if it's something you can find at Google at the same speed.
> But my notes are mine, meaning I know what I can't remember or in
> which form I need some piece of information. Sometimes, I write a long
> article about something and other times some bullet points are good
> enough. When I share my notes on a team/organization I try to make
> sure the context is clear. It's a bit like code: it's read by an order
> of magnitude more often than written/changed.
>
> -- [Hacker News](https://news.ycombinator.com/item?id=23724730),
> trimmed

#### Exhibit E

> There are two main problems that documentation authors may have with
> API docs:
>
> The generated API documentation lives in isolation, separate from the
> rest of your document content. This can lead to difficulties in
> maintaining a cohesive and integrated document that provides a
> holistic view of your product or service.
>
> When trying to integrate API documentation with the rest of your
> content, manual editing is often required. However, often there is no
> ability to enhance autogenerated reference with manually written
> parts.
>
> -- [API documentation \|
> Writerside](https://www.jetbrains.com/help/writerside/api-documentation.html)

#### Exhibit F

> i keep detailed journals of every project i do, these days. partly
> because i’m so scattered lately that a project might sit for years so
> being able to pick up where i left off is the only way it will ever
> progress. but also because writing it down helps me think about it.

#### Exhibit G

> Documentation is extraordinarily difficult to create. You need to
> anticipate the potential questions and answer them and anticipate all
> the potential perspectives and answer them from that perspective.
