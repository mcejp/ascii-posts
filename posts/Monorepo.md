---
layout: post
render_with_liquid: false
date: 2025-03-14
title: Monorepo
unlisted: true
---

Something to ask yourself: do we need different release cycles for these
different components?

Pros:

- merge requests spanning sub-projects
- global refactoring; breaking changes
- easier to search

Cons:

- CI bound to be either inefficient, or messy with a lot of rules
- commit churn can make history difficult to navigate
- disk space requirements, performance penalty (depending on size)

Insightful discussions:

- <https://news.ycombinator.com/item?id=39903958>
