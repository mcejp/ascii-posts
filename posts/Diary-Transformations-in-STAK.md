---
layout: post
render_with_liquid: false
date: 2025-04-20
title: "Diary: Transformations in STAK"
unlisted: true
---

Want to have convenience forms such as:

``` scheme
(for/range (i 0 NUM-BLDGS)
  body...)
```

Essentially equivalent to:

``` scheme
(define i 0)
(define #max NUM-BLDGS)
(while (< i #max)
  body...
  (set! i (+1 i)))
```

In this case it seems like a good use-case for a simple pattern-based
macro system.

This solution is not without issues:

- `#max` will conflict in case of nested loops... in absence of block
  scopes, it should be a gensym.
- `i` will escape into the surrounding scope. Corollary: the same macro
  cannot be used again with the same variable in the same scope -- it
  will be considered as redefinition, an error.

All that being said, what if I really don't want to go into
spec'ing/implementing a macro language? Is there a way to still enrich
language **without** spilling this complexity into the compiler, reusing
pre-existing primitives?

Yes, there is: implement a transformation 'hook' before parsing
statement/expression, and put all transformations into another Hy
module, so that the compiler remains deliciously hackable. This crude
design will impose some limitations, but should be workable. For
example, to expand a statement into multiple statements, they can be
wrapped in `(when 1 ...)`. This will come at the cost of size + runtime
overhead (as have many previous decisions), but that's okay for the
moment.

As for implementing the transformations themselves, we will take the
same approach as used in the compiler itself (hy.model-patterns).
Unfortunately we don't have `syntax-case` (or the more advanced
`syntax-parse`) in Hy. Maybe this would be a good opportunity to take a
shot at implementing it.
