---
layout: post
render_with_liquid: false
date: 2024-06-21
title: Git
unlisted: true
---

### Merge branch but discard its history

1.  checkout target branch (e.g., `master`)
2.  `git merge --squash SOURCE_BRANCH`

Alternative

1.  check out source branch (e.g., `ci`)
2.  soft reset to target branch (e.g., `master`)
3.  commit
4.  delete `master` & rename `ci` to `master`
5.  done!

### Sort uncommited files by modification time

Staged:

    git diff --name-only --cached | xargs stat -c '%y %n' -- | sort

Modified, unstaged:

    git ls-files -m | xargs stat -c '%y %n' -- | sort

Untracked (respecting .gitignore)

    git ls-files -o --exclude-standard | xargs stat -c '%y %n' -- | sort

### Spin subdirectory off into new repo

This works well: <https://stackoverflow.com/a/17864475>

(`git subtree` is safe, it creates a new branch)
