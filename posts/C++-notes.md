---
layout: post
render_with_liquid: false
date: 2024-05-09
title: C++ notes
unlisted: true
---

## C++ on embedded platforms

### Reasons for C++ over C

- Easier to write robust code, e.g.
  - better type system in general
  - `std::optional<T>` instead of `T value, bool value_valid`
  - distinction between 0 & nullptr
- Simple structs are simple to use
- Classes and namespaces are nice
- `auto` is nice
- for-iteration over containers is nice

### Talks about embedded C++

- [Curiosity's FSW Architecture: A Platform for Mobility and Science,
  Dr. Kathryn Weiss, NASA
  JPL](https://www.youtube.com/watch?v=9jVt5vb68xA)

### Some drawbacks of C++

- Allows you to leave unitialized POD variables, particularly pointers
  (=\> use references wherever possible)
- Allows you to write heap of mess that nobody (including you)
  understands
- C++ libraries require a complete-ish implementation of the C standard
  library underneath (this can suck on niche platforms)

## Embed any file in source code

    xxd -include <filename>

(discussion: <https://unix.stackexchange.com/a/176112>)

## \#pragma once

Pros:

- no risk of collision of guards
- less noise

Cons:

- compiler can get confused due to symlinks (unless it checks i-node
  number?)
- if the same file exists in multiple include paths (which it
  shouldn't), this will fail
- not standard

## Proper modulo (rounding towards -inf)

See
<https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/divmodnote-letter.pdf>
