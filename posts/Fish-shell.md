---
layout: post
render_with_liquid: false
date: 2026-09-06
title: "Fish shell"
unlisted: true
---

### Add to PATH (permanently)

    fish_add_path ~/.local/bin

### Foreach

``` fish
for THING in foo bar baz
    mkdir test$THING
    mv test$THING.cpp test$THING
end
```

### Function editor

    funced name

OR

    EDITOR="code -w" funced name

*then don't forget to `funcsave`!*

(how to backup/synchronize/...? stored in
`funcsave: wrote ~/.config/fish/functions/<name>.fish`)

#### Function argument processing

``` fish
if test (count $argv) -ne 1
    echo "usage: ./release-gizmo <version>"
    return 1
end

# then use $argv[1]
```

#### Optional arguments

``` fish
if test (count $argv) -lt 1 -o (count $argv) -gt 2
    echo "usage: conan-fs-sync-timing-wrt <version> [release_location]"
    return 1
end
```
