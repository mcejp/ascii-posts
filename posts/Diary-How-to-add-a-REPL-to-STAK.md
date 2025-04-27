---
layout: post
render_with_liquid: false
date: 2025-04-15
title: "Diary: How to add a REPL to STAK"
unlisted: true
---

We start out having a [compiler, linker and bytecode
interpreter](https://github.com/mcejp/STAK) -- all very standard,
by-the-book design. How to add REPL without having to reinvent the
tooling? Moreover, it should work on all platforms where the interpreter
can run (desktop, MS-DOS, consoles)

From the back: the interpreter will need a to incorporate a debug
server, to allow manipulation of execution as well as of the code
itself. For desktop, this can be a line-oriented text protocol on top of
TCP. The interpreter has no clue about the structure of the program, so
it can only provide low-level primitives. The debugger side will have to
figure out all the rest.

Let's think of the simplest case where the interpreter starts out as a
blank slate. It needs to be told to start out in suspended state (this
can also be achieved by a dummy program containing a single `'brk`
opcode). The user enters a statement into the REPL; to allow compound
statements, the REPL can continue to accept input until parentheses are
balanced. The REPL calls the compiler, wrapping the entered statement in
a dummy function declaration. Good, except this will not work for
variable declarations: they would not be seen by following statements!
It will also not work for function declarations, since they can not be
nested. There is a simple solution -- have the REPL detect these forms
and compile them in a global context.

The compiler produces a compilation unit. The unit is very easily
relocatable:

- globals are referenced by name
- functions are referenced by name
- branches are always relative
- locals are, well, local
- constants are numbered locally as well (via `'constants-offset`)

The linker is then invoked to produce a linked program. The program
contains a table of functions and marks one of them as the main
function. The program must be loaded into the interpreter. The
interpreter is instructed to begin executing at the start of the main
function. How to tell the interpreter where to stop? Some ideas:

- a\) place a breakpoint after the last instruction of `main` (but what
  if another function begins there?)
- b\) construct an artifical `real-main` which will just call `main` and
  then break
- c\) instrument the compiler to insert a `'brk` at the end of `main`
- d\) append a `(break)` statement to the user input

Option d) seems like the most pragmatic one.

When the breakpoint is encountered, the interpreter will suspend
execution and inform the REPL. The REPL must pop the top-of-stack and
print it. But this will only work for one iteration. Then what?

User enters another statement. First of all, the compiler needs to be
told about previously defined global variables (it raises an error upon
encountering an undeclared variable, so we cannot wait until link time).
The linker needs to be told about previously defined functions and
globals. For the moment, let's not permit updating previously defined
functions (though a special case will be necessary to permit redefining
`main`). The linker needs to run in an "incremental mode", taking into
consideration:

- number of previously defined functions, globals, constants (reminder:
  constants are not de-duplicated across functions, so only the total
  count is relevant)
- length of existing bytecode

The linker will thus produce a "program fragment", whose bytecode can be
loaded starting at the end of the previous program, and its
function/global/constant tables appended to the existing tables.
(Optimization opportunity: if `main` was the last function in the old
program, its bytecode can be overwritten, and its function table entry
replaced). As we have discovered, to permit iteration, the linker will
also need to provide:

- the (updated) function table
- the (updated) global table

The REPL now instructs the interpreter to load the program fragment with
the respective table/code offsets. It finds the new main function and
jumps to it.

### How to reconcile global x local x REPL

- Locals can be initialized with an arbitrary expression
- Globals can only be initialized with a literal integer value
  - This makes sure that all globals are initialized before first use in
    a linked program
  - Otherwise the rule could be relaxed and globals initialized by code
    like locals (but it would be less efficient for the vast majority of
    cases)
- In REPL, we want to define values with an expression

At the same time:

- The execution model requires REPL variables to be globals, since all
  local contexts cease to exist after execution
  - Maybe they shouldn't?
  - What is our goal in the bigger picture, i.e. w.r.t. debugging a
    larger program
    - Indeed we will want to stop in the middle of a function and
      potentially execute entered code

If the compiler had a "REPL mode" what would it do:

- allow statements in top-level (implicit `main`)
- globals initialized with expression

### Additional interpreter state

- ~~`bool Thread::suspended`~~ -- already have it
