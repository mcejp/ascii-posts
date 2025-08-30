---
layout: post
render_with_liquid: false
date: 2025-08-19
title: "Git"
unlisted: true
---

### Delete directory from history

    git filter-repo --invert-paths --path filename

Can use `--refs master..HEAD` to only change stuff between master and
current HEAD

### Merge branch but discard its history (add a single commit)

1.  checkout target branch (e.g., `master`)
2.  `git merge --squash SOURCE_BRANCH`

Alternative

1.  check out source branch (e.g., `ci`)
2.  soft reset to target branch (e.g., `master`)
3.  commit
4.  delete `master` & rename `ci` to `master`
5.  done!

### Separate a change from a commit and move it earlier in history

- `git rebase -i HEAD~2`
- insert a `break` command *before* the commit in question
- cherry pick the change(s) to separate, commit with new message
- continue rebase; the rest of the original commit will be applied now

### Separate a change from a commit and move it later in history

- `git rebase -i HEAD~2`
- insert a `break` command *before* the commit in question
- cherry pick the change(s) to separate, commit with new message
- continue rebase; the rest of the original commit will be applied now
- rebase again, this time move the newly created commit as desired

### Set all commit dates to author dates

    git filter-branch --env-filter 'export GIT_COMMITTER_DATE="$GIT_AUTHOR_DATE"'

(<https://stackoverflow.com/questions/28536980/git-change-commit-date-to-author-date>)

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
