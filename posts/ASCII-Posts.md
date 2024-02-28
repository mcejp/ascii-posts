---
layout: post
render_with_liquid: false
date: 2024-02-28
title: ASCII Posts
unlisted: true
---

*ASCII Posts* are snippets of my personal notes. They are exported
periodically from my personal knowledge base. They are published in the
hope that they may be of use to someone, without requiring the effort of
full-scale blog articles.

The original idea was to use 80-column monospace ASCII for the posts,
but it looked like ass. So, now it's Markdown instead. Since the posts
are rendered by GitHub, all features of GitHub Flavored Markdown can be
used, such as [Mermaid
diagrams](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams).
For now, only text content is exported, no images.

Although I have a [blog](https://mcejp.github.io) based on Jekyll, a
static-site generator, I wanted to completely avoid the extra complexity
involved in it -- at least for the proof-of-concept. It also helps in
distinguishing the higher-effort blog posts from these quicker notes.

Publishing the notes as a GitHub Wiki gives us all of these, with
minimum effort:

- hosting & rendering of Markdown
- deploy with a `git push`
- table of contents (not a great one, but it's a start)
- version history

Publishing as Gists would additionally get us comments, but at the cost
of ugly URLs and no automatic TOC.

It works like this:

- the 'master copy' of each post is one note in my Joplin notebook
- [the script](https://github.com/mcejp/ascii-posts/blob/master/main.py)
  periodically exports the latest version of all posts using the [Joplin
  Data API](https://joplinapp.org/help/api/references/rest_api/)
- the posts are pushed to a GitHub Wiki

### Flow chart test

``` mermaid
graph LR;
    A-->B;
    A-->C;
    B-->D;
    C-->D;
```

### Unsolved issues

- [small repositories' Wikis are excluded from search engine
  indexing](https://github.com/orgs/community/discussions/4992#discussioncomment-1448177)
- different interpretations of newlines between Joplin & GitHub
- post titles must be valid file names (no forward slashes)
  - work-around; substitute special characters with their Unicode
    look-alikes
