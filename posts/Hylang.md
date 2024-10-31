---
layout: post
render_with_liquid: false
date: 2024-10-29
title: Hylang
unlisted: true
---

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

(In STAK, we implemented our own)
