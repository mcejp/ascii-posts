---
layout: post
render_with_liquid: false
date: 2024-04-01
title: ASCII Posts
unlisted: true
---

*ASCII Posts* are snippets of my personal notes. They are exported
periodically from my personal knowledge base. They are published in the
hope that they may be of use to someone, without requiring the effort of
a polished blog article on my part.

The original idea was to use 80-column monospace ASCII for the posts,
but the reading experience was poor. So it's Markdown instead. In the
first iteration, it was published as a GitHub Wiki; although I have a
[blog](https://mcejp.github.io) based on Jekyll, a static-site
generator, I wanted to completely avoid the extra complexity involved in
it. I also felt that this helped to distinguish the higher-effort blog
posts from these quicker notes.

Publishing the notes as a GitHub Wiki had these features, with minimum
effort:

- hosting & rendering of Markdown
  - with GitHub extras, like rendering of graphs
- deploy with a `git push`
- table of contents (not a great one, but it's a start)
- version history

It definitely did its job as a proof-of-concept, but it was not without
drawbacks:

- post titles had to be valid file names
  - significant characters like slashes needed to be substituted by
    look-alike Unicode characters
- it turns out that [small repositories' Wikis are excluded from search
  engine
  indexing](https://github.com/orgs/community/discussions/4992#discussioncomment-1448177)

The second generation is a "proper" Jekyll website with some custom
styling, hosted with GitHub Pages. It works like this:

- the 'master copy' of each post is one note in my Joplin notebook
- [the script](https://github.com/mcejp/ascii-posts/blob/master/main.py)
  periodically exports the latest version of all posts using the [Joplin
  Data API](https://joplinapp.org/help/api/references/rest_api/)
- the posts in Markdown are pushed to a specific branch
- a CI job renders the Jekyll website and publishes it to GitHub Pages

### Unsolved issues

- in Joplin, line breaks are preserved, which is not standard CommonMark
  behavior
- SEO aspects
  - markup in front page
