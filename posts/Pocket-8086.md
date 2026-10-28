---
layout: post
render_with_liquid: false
date: 2026-10-24
title: "Pocket 8086"
unlisted: true
---

Similar to: IBM PS/2 Model 30 (1987)

| Aspect | Pocket 8086 | IBM PS/2 Model 30 (8530-002/021) |
|----|----|----|
| Introduced | 2024 | April 1987 |
| CPU | NEC V30 (8086-compatible, with 80186 instructions), switchable 4.77/10 MHz | Intel 8086, 8 MHz |
| RAM | 768 KB (640 KB base + 128 KB UMB) | 640 KB |
| Bus / expansion | ISA expansion via a separate add-on card | Three 8-bit ISA slots |
| Graphics | TVGA9000i VGA with 512 KB VRAM (replaceable card) | MCGA (VGA-like, but limited to 320×200 in 256 colors, 640×480 in mono) |
| Display | Built-in 7" 800×480 IPS (one source says 6"), plus VGA out | External monitor required |
| Audio | OPL3 (YMF262) FM sound | PC speaker only |
| Storage | 512 MB CF card; USB mass storage | 3.5" 720 KB floppy; optional 20 MB hard disk |

### USB flash drive

The surest way to make it work is to write a 1.44M floppy image to the
flash drive:

``` sh
mkfs.msdos -C floppy.img 1440
sudo mkdir -p /media/floppy
sudo mount -o loop,rw,umask=000 floppy.img /media/floppy
...copy content to /media/floppy/...
sudo umount /media/floppy
sudo dd if=floppy.img of=/dev/sda
```

It needs to be plugged in when the device is powered on. It will be
mounted as drive `D:`.

To be seen:

- what is the size limit
  - 8 MB works, maybe 32 MB then (limit of FAT12), or 504 MB (1024
    cylinders, 16 heads, 63 sectors)
  - 512 MB works: `mkfs.msdos -F16 /dev/sda 524288`
- if the USB controller
  ([CH375](https://www.wch-ic.com/products/CH375.html)) is flexible
  enough to implement support for other devices: mice, card readers,
  MIDI keyboards... or even make the 8086 show up as a mass storage
  device to a PC
  - [USB mass storage
    example](https://forum.vcfed.org/index.php?threads/book-8088-discovery-and-modification-thread.1245155/post-1343495)
  - [mouse
    example](https://github.com/joshuashaffer/book8088-ch375mouse-poc)

### BIOS/driver replacement

- [FreddyV DOS Driver for ISA USB
  v0.22](https://www.vogonsdrivers.com/getfile.php?fileid=1991&menustate=0)

### FPU emulation issue

It seems that code compiled with Open Watcom using floating-point
instructions with fallback emulation (the default; `-fpi`) locks up the
CPU instead of using the fallback.

### HW mods

- [Wi-Fi using
  ESP8266](https://forum.vcfed.org/index.php?threads/book-8088-discovery-and-modification-thread.1245155/post-1443946)

### See also

- [Book 8088 discovery and modification thread \| Vintage Computer
  Federation
  Forums](https://forum.vcfed.org/index.php?threads/book-8088-discovery-and-modification-thread.1245155/)
  (especially later pages)
