---
layout: post
render_with_liquid: false
date: 2024-03-26
title: Jekyll tips & tricks
unlisted: true
---

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
