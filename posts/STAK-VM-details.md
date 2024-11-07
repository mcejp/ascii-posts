---
layout: post
render_with_liquid: false
date: 2024-11-03
title: STAK VM details
unlisted: true
---

## Instruction set

``` scheme
(zero)             ; implemented
(drop)             ; implemented

(getlocal idx)     ; implemented
(setlocal idx)     ; implemented

(getglobal idx)    ; implemented
(setglobal idx)    ; implemented

(getconst idx)     ; implemented

(call:func func_idx nargs)     ; implemented
(call:ext ext_func_idx)        ; implemented
(ret nvals)                    ; implemented
(ret:void)
(jmp offs16)                   ; implemented
(jz  offs16)                   ; implemented

; arithmetic, logic, comparisons -- for now implemented with call:ext
(add)
(sub)
(mul)
(div)

(lt)
(gt)

; arrays?
(getelem)
(setelem)
```

### ISA optimization opportunities

(we are not doing any of these as we want to minimize amount of
implementation code to avoid ossification (at least for now))

- `(const N)` `(add N)` for 8-bit constants
- `(one)` `(two)`
- `(dup)`
- `(getlocal)` could always be referenced to stack pointer if we keep
  track of temporaries during compilation
- `(getlocal:N)` `(getconst:N)` `(setlocal:N)` for low values of N
- `(ret-zero)` = `(zero) (ret 1)`

## Stack layout

Stack layout for function call

    Locals
    Temporaries
    Args --> become first N locals of called function

Function entry:

    old_frame->pc = pc
    old_frame->fp = fp
    fp = sp - func->argc
    sp += num_locals

Function return:

    ret_val = STACK[--sp]
    sp -= func->num_locals + func->argc
    STACK[sp++] = ret_val
    fp = old_frame->fp
