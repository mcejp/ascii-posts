---
layout: post
render_with_liquid: false
date: 2025-04-21
title: "STAK: Tracking result arity in compiler"
unlisted: true
---

I.e. how to know how many values were produced by an expression? How to
know if I need to push a `zero` before `ret`?

Answer: Each branch of `compile-statement` keeps track of the number of
elements that it has left on the stack. `compile-expression`, on the
contrary, takes `expected-values` as a parameter.

`compile-statements` loops over statements in a function and discards
leftovers in between each, but not after the last one -- that number is
returned to `compile-function-body`. The latter can then easily make
sure that at least 1 value is being returned:

``` hy
(defn compile-function-body [ctx body]
  (setv num-values-on-stack
    (compile-statements ctx body))

  (unless num-values-on-stack
    ;; make sure we're returning something
    (ctx.emit 'zero)
    (setv num-values-on-stack 1))

  (ctx.emit 'ret num-values-on-stack)
  num-values-on-stack)
```

The last piece of the puzzle is making sure the number of values
returned matches the number of values expected at the call site. This
cannot be done until link time. Unresolved `'call`s therefore include
the number of return values expected. The linker can then check this,
because the number of returned values is statically known (it is
conveyed by a function's `retc` property)

Source: <https://github.com/mcejp/STAK/blob/main/compile.hy>
