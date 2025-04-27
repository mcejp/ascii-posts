---
layout: post
render_with_liquid: false
date: 2025-04-27
title: "Diary: Framing in STAK listener protocol"
unlisted: true
---

My favorite framing algorithm is [Consistent Overhead Byte Stuffing
(COBS)](https://en.wikipedia.org/wiki/Consistent_Overhead_Byte_Stuffing),
because of its elegance and, I guess, best average-case overhead. It has
one disadvantage, though. Before sending a byte, it needs to look at up
to 254 following bytes. This could be unpleasant on the DOS side. Let's
look for something with a shorter context window.

[HDLC
framing](https://en.wikipedia.org/wiki/High-Level_Data_Link_Control#Asynchronous_framing)
instead uses a special escape byte. It's quite nifty in how it works,
because it can also be used for escaping XON/XOFF (software flow control
bytes) if we end up using those.

By the way, does GDB define a framing protocol? [Yes it
does](https://ftp.gnu.org/old-gnu/Manuals/gdb/html_node/gdb_129.html),
but it's all ASCII (using hex numbers for blob transfers. eugh.)

So HDLC framing works like this:

- `0x7D`, `0x7E` are reserved bytes
  - if you are using software flow control, add XON (`0x11`) + XOFF
    (`0x13`) to this set
  - generally, you can add anything else that has special meaning on the
    wire
- when a reserved byte is encountered inside the frame:
  - emit `0x7D`
  - emit the byte xor `0x20`
  - examples:
    - `0x7E` -\> `0x7D 0x5E`
    - `0x7D` -\> `0x7D 0x5D`
- `0x7E` delimits frames
  - it's not clear to me if it is mandated to appear *before* the first
    frame, but it would make sense, so that you can always
    re-synchronize
  - therefore, the transmitter needs to keep an additional bit of state
    to know if the first delimiter has already been sent. or just append
    it before *and* after each frame.
- the "abort sequence" `0x7D 0x7E` ends a packet with an incomplete
  byte-stuff sequence, forcing the receiver to detect an error

Related RFC: <https://www.rfc-editor.org/rfc/rfc1549.html#section-4>
