---
layout: post
render_with_liquid: false
date: 2024-07-21
title: "Sphinx tips & tricks"
unlisted: true
---

Good looking theme: [Furo](https://github.com/pradyunsg/furo)

- example: <https://python-gitlab.readthedocs.io/>
- huge fonts though, look at
  <https://github.com/pradyunsg/furo/discussions/385>

Q: How to serve live preview on Windows without going crazy?

- A: Use WSL and then it's straightforward

Q: Example of Sphinx-\>GitLab pages CI?

Q: Example of Sphinx-\>GitHub Pages CI?

- A:
  <https://github.com/mcejp/propel/blob/master/.github/workflows/pages.yaml>

### Alternatives

- Sphinx (<https://docs.kernel.org/>)
- GitHub/GitLab Wiki? Is this usable as static site generator?
- [VitePress](https://vitepress.dev)
- mdBook (<https://doc.rust-lang.org/book/>,
  <https://docs.hyperdeck.io/>)
- mkdocs (<https://hsutter.github.io/cppfront/>)
- GitBook/HonKit
- Any wysiwyg?
- hugo
- "one of the main reasons why we selected docusaurus is because of the
  search engine, far better compared with the mkdocs."

### GitLab: Publish docs on tag push, use tag name as version

#### .gitlab-ci.yml

    my_job:
      (...)
      only:
        - tags

#### config.py

    import os

    (...)

    version = os.getenv("CI_COMMIT_TAG", default=None)
    release = version

    (...)

    # This is the default, but just to be sure:
    # html_theme_options = {
    #     'display_version': True,
    # }

### Issue: sphinx-autobuild doesn't refresh on Python code change

Add `--watch=<dir>`
