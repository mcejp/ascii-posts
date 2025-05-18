---
layout: post
render_with_liquid: false
date: 2025-05-17
title: "Pocket 8086"
unlisted: true
---

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
- if it works after mounting /dev/sda directly (Linux doesn't seem to
  recognize that the filesystem should be limited to 1.44 MB in that
  case)
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
