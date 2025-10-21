---
layout: post
render_with_liquid: false
date: 2025-10-19
title: "STAK: Tracking result arity in compiler"
unlisted: true
---

##### 2025-04-21

I.e. how to know how many values were produced by an expression? How to
know if we need to insert a `zero` before `ret`?

Answer: Each branch of `compile-statement` keeps track of the number of
elements that it has left on the stack. `compile-expression`, on the
contrary, takes `expected-values` as a parameter; the only case where it
is not 1 is inside a `(define foo bar (...))` form. How can
`(values 1 2 3)` work, then? Cleverly: by being a statement, not an
expression.

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

<!-- Source: https://github.com/mcejp/STAK/blob/main/compile.hy -->

##### 2025-10-19

With the introduction of `cond`, the flaws of the initial solution
became more problematic. But a relatively simple solution was possible
by tweaking some of the rules:

- when evaluating an expression in the role of a statement, do not
  constrain the number of values
- when evaluating a function call, if the number of values is
  unconstrained, assume 1

This then permits the implementation of the `cond` expression with the
following rules:

- for `cond` to be usable as an expression, i.e. to return a nonzero
  number values, it must contain a "catch-all clause" (whose condition
  is the literal `1`)
- only one catch-all clause may appear and it must be the last clause
- if a catch-all clause is present, then the number of values produced
  by each clause must be the same and it will be the overall number of
  values produced by the expression
- if no catch-all clause is present, all values produced by the clauses
  are discarded and the expression returns no values (it can still be
  used as a statement)
