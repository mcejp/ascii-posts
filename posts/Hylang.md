---
layout: post
render_with_liquid: false
date: 2025-04-24
title: "Hylang"
unlisted: true
---

### Command-line argument parsing

See
[hyrule.parse-args](https://hylang.org/hyrule/doc/v1.0.0#hyrule.parse-args)

### Convention for comments

> - Comments that start with four semicolons, `;;;;`, should appear at
>   the top of a file, explaining its purpose.
> - Comments starting with three semicolons, `;;;`, should be used to
>   separate regions of the code.
> - Comments with two semicolons, `;;`, should describe regions of code
>   within a function or some other top-level form, while
>   single-semicolon comments, `;`, should just be short notes on a
>   single line.
>
> -- <https://lisp-lang.org/style-guide/#comment-hierarchy>

### Iterate over DAG nodes in topologic order (naive but easy-to-understand algorithm)

``` scheme
(defn depth-first [tree]
  "Iterate the nodes of a DAG in depth-first order without repetition"
  (yield :from (depth-first* tree #{})))

(defn depth-first* [node visited]
  (when (in node visited)
    (return))
  (visited.add node)

  (for [dep node.deps]
    (yield :from (depth-first* dep visited)))
  (yield node))

;; DEMO

(import dataclasses [dataclass])

; node needs to be comparable and hashable; here we fall back to id-based hashing
(defclass [(dataclass :eq False)]
          Node []
  #^ str name
  #^ list deps)

(setv wren    (Node "WREN" [])
      ltim    (Node "LTIM" [wren])
      wren-du (Node "WREN_DU" [ltim wren]))

(for [node (depth-first wren-du)]
    (print node.name))
```

### Q: 2 or 4 spaces for indent?

A: Official repo uses 2

### Q: Group imports (use single `import` form)?

A: Yes. FWIW, Hy repo sometimes does, sometimes not.

### Q: How to have a macro receive kwargs and propagate them into emitted code?

``` hy
;; rest-args can be any combination of positional and keyword arguments,
;; they will be just copied over token-by-token
(defmacro something [foo bar #* rest-args]
  `(do-something ~foo ~bar ~@ rest-args))
```

### Q: How to print indented S-exprs?

(In STAK, we implemented our own)

### Q: How to de/serialize dataclasses to S-exprs?

Our state-of-the-art -- pretty awful:

- [serialize](https://github.com/mcejp/STAK/blob/main/models.hy#L69)
- [deserialize](https://github.com/mcejp/STAK/blob/main/models.hy#L30)
