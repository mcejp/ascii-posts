---
layout: post
render_with_liquid: false
date: 2024-01-03
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
- C++ libraries require a complete-ish underlying C library

## Embed any file in source code

    xxd -include <filename>

## \#pragma once

Pros:

- no risk of collision of guards
- less noise

Cons:

- compiler can get confused due to symlinks
- not standard
