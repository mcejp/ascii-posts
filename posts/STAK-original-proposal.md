---
layout: post
render_with_liquid: false
date: 2023-09-04
title: "STAK original proposal"
unlisted: true
---

    - sole type i16
    - stack machine
    - local variables (by index)
    - global variables

    - threads? desirable. (fixed number)
    - code paging?
        - ok, relocate at load. but some globals should be shared etc... not so simple
        - or just add module_index wherever relevant?
          - but still need to resolve globals
        - OR JUST OMIT IT NOW FOR SIMPLICITY

    - arrays: allocated on heap; user code responsible for freeing
      e.g.
        my_arr = new_array(30)
        print(my_arr)       ;; prints numeric index of newly allocated array
        my_arr[5] = 10
        resize_array(my_arr, 10)
        del_array(my_arr)   ;; index is made available again

        (set my-arr (new_array 30))
        (print my-arr)
        (set (get my-arr 5) 10)
        (resize_array my-arr 10)
        (del_array my-arr)

    - alt: all arrays declared statically
      we can allow resizing, or even not

        array my_arr[30]

        print(my_arr)       ;; prints numeric index
        my_arr[5] = 10
        resize_array(my_array, 10)
        resize_array(my_array, 0)       ;; effectively free the held memory

    - where do pre-initialized arrays fit in?

    - strings: same as array but uint8 elements (oof?)
        str = "hello"
        prints(str)
        new_str = strcat(str, " world")
        prints(new_str)
        del_str(new_str)

    - alt: force all strings to use pre-allocated buffers

        str my_str[30]

        sprintf(my_str, "hello %s", "world")
        prints(my_str)

        (#str my-str 30)

        (sprintf my-str "hello %s" "world")
        (prints my-str)

        (const 11)      ;; my_str
        (const 15)      ;; "hello %s"
        (const 16)      ;; "world"
        (call.ext sprintf 3)
        (const 11)      ;; my_str
        (call.ext prints 1)


    I/O:
        read-only set of files adressed by name (or maybe not in compiled BC?)
          open, readat, close

        read-write storage by slot index (like Java RMI?)
          save_array(index, array)
          load_array(index, array)      ;; returns real length

    ### explicit non-goals

    - useful as native instruction set
    - self-hosting compiler
    - systems programming (loading other programs etc.)

    ## compilation model

    - core module (any number of units)
    - loadable modules (use functions & globals from core + add their own)
      - how to call into them? do they export functions by name?

    - what if single module, transparently paged?

    ## how to build compiler

    ### outline

    - collect functions & globals across compilation units
    - assign IDs
    - link together
    - save map to compile loadable modules against

    ### compilation step

    - parse constants.json
    - parse S-expr via hy.load
    - unit = Unit(globals={}, functions={})
    - for TLF in top-level forms:
        - match (define <name> <integer-literal>)
        - match (define <prototype> <body> ...)
            - create function = dict(name, argc, constants, locals, body)
            - parse body[]

    compile function body:

    - for TLF in forms:
        - match (set! <name> <value>)
            - compile expression
            - declared global?
                - yes -> emit `setglobal` by name
                - no -> find/assign variable name, emit `setlocal` by index
        - else compile expression
            - and drop result from stack -- unless last expression in the function

    - if last form was a statement, push dummy return value on stack

    compile expression:

    - match literal
        - find/assign constant index
        - emit `getconst`
    - match name
        - is builtin constant?
            - handle as a constant
        - declared global?
            - yes -> emit `getglobal` by name
            - no -> find variable name, emit `getlocal` by index
    - match (<callee> <args> ...)
        - evaluate arguments
        - emit `call`

    ### linking step

    - parse builtins.json
    - assign indexes to functions
    - assign indexes to globals (+ resolve initial value which must be unique)
    - resolve calls to `call:func`, `call:ext`
    - resolve `getglobal`/`setglobal` to indexes
    - in principle could also check arity of function calls
    - concatenate function bytecode

    ## simplification opportunities

    - validate arity at compile time, keep no trace of it at runtime

    - built-in operators are actually externals (no problem if single data type)

    - a function's constants spilled as locals on function entry
        - it actually complicates function prologue & data strcturure. the only simplification is removal of `getconst`


    # code

    ## builtins.json

    {
        "fill-rect": {id: 0, argc: 5},
        "pause-frames": {id: 1, argc: 1},
    }

    ## constants.json

    {
        "COLOR:BLACK": 0,
        "COLOR:WHITE": 15,
        "W": 320,
        "H": 240
    }


    ## test1.scm: tests function calls, constants, external calls

    (define (draw-splash)
        (fill-rect COLOR:WHITE 0 0 W H)
    )

    (define (main)
        (draw-splash)
        (pause-frames 100)
    )


    ## test1.unit

    (globals)

    (functions
        (function "draw-splash"
            (argc 0)
            (constants 15 0 320 240)
            (locals 0)
            (body
                (getconst 0)
                (getconst 1)
                (getconst 1)
                (getconst 2)
                (getconst 3)
                (call "fill-rect" 5)
            )
        )
        (function "main"
            (argc 0)
            (constants 50)
            (locals 0)
            (body
                (call "draw-splash" 0)
                (getconst 0)
                (call "pause-frames" 1)
            )
        )
    )


    ## test1.prog

    (bytecode
        (getconst 0)
        (getconst 1)
        (getconst 1)
        (getconst 2)
        (getconst 3)
        (call.ext 100 5)
        (ret.void)

        (call.func 0 0)
        (getconst 0)
        (call.ext 101 1)
        (ret.void)
    )

    (constants
        15 0 320 240
        50
        )

    (globals)       ;; init values for globals go here

    (functions
        (defun  ;; draw-splash
            (argc 0)
            (locals 0)
            (bytecode-offset ...)
            (constants-offset 0)
        )
        (defun  ;; main
            (argc 0)
            (locals 0)
            (bytecode-offset ...)
            (constants-offset 4)
        )
    )

    (main-function 1)


    ## test2.scm: tests globals

    (define *color* 0)

    (define (draw-splash)
        (fill-rect *color* 0 0 W H)
    )

    (define (main)
        (draw-splash)
        (pause-frames 10)
        (set! *color* 1)
        (draw-splash)
        (pause-frames 10)
        (set! *color* 2)
        (draw-splash)
        (pause-frames 10)
        (set! *color* 3)
        (draw-splash)
        (pause-frames 10)
        (set! *color* 4)
    )


    ## test3.scm: tests locals, loops

    (define (draw-splash color)
        (fill-rect color 0 0 W H)
    )

    (define (main)
        (define color 0)
        (while (<= color 15)
            (draw-splash)
            (pause-frames 10)
            (set! color (+ color 1))
        )
    )


    ## test4.scm

    (define (main)
        (prints "hello world")
    )


    ## test-graphics.scm

    (define res-logo 999)

    (embed logo "logo.png")
    ;; might be problematic because palette must match
    ;; can enforce in code: https://stackoverflow.com/a/9833540
    ;; or require ahead-of-time conversion which will add a custom header

    (define (main)
        (set-video-mode W H)

        (draw 0 0 logo)

        ;; resource is uncompressed image with custom header?
        ;; should we implement strings/buffers first?
        ;; Q: why not just (include "logo.png") ?
        (set! res-logo (load-resource "logo"))

        )

    {
        embeds: ["image:32:32:uhfifh3489hr8r3hohewh823heoddnuweh298309jdjnds-0ood0o;09jf"],
    }

    in code: embed index is known at compile, but must be relocated on link. let's call it `getembed`
