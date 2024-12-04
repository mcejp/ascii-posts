---
layout: post
render_with_liquid: false
date: 2024-12-04
title: Allwinner D1s/F133 notes
unlisted: true
---

### Q&A

#### Q: Bare-metal debugging possible?

Apparently: <https://linux-sunxi.org/Allwinner_Nezha#JTAG> -- but what
is the physical connection?

#### Q: What is the pre-flashed image in MangoPi MQ?

A: None: there is no persistent memory besides the SD card

#### Q: What is BOOT0?

A: it is the [Allwinner SPL (Secondary Program
Loader)](https://github.com/smaeul/sun20i_d1_spl).

It is something that you link into your boot image. Apparently U-Boot
obsoletes it:
<https://github.com/smaeul/u-boot/releases/tag/d1-2022-10-31> (but is it
in mainline U-Boot too?)

Searching for `get_pmu_exist` (appears in boot0 output) yields a lot of
other interesting links.

Some MQ-specific configuration here:
<https://github.com/amessier/sun20i_d1_spl/commit/234b2e905a88f29db91768a25ad1c779594a598e>

#### Q: How to copy .img (IMAGEWTY) files to SD card on Linux?

A: Must use [OpenixCard](https://github.com/YuzukiTsuru/OpenixCard)
*dump* feature.

#### Q: Is OpenSBI needed for bare-metal development?

Not really, it's a way to have platform firmware in H-mode and OS or
hypervisor in S-mode. Bare-metal code can just run in M-mode directly.

#### Q: xfel vs sunxi-fel

sunxi-fel -\> `Invalid command ddr`

I guess it doesn't support the F133

#### Q: Can switch between RV64 and RV32

No, the C906 core doesn't support this, neither in S- or U-mode.

#### Q: In light of above, can we at least convince GCC that 32-bit pointers would do?

There is a proposal:
<https://lpc.events/event/17/contributions/1475/attachments/1186/2442/rv64ilp32_%20Run%20ILP32%20on%20RV64%20ISA.pdf>

Is it ratified or at least widely accepted, though?

> A future version of this specification may define an ILP32 ABI for the
> RV64 ISA, but currently this is not a supported operating mode

Might need to build toolchain from source. TBC

- <https://lwn.net/Articles/932290/>
- <https://lwn.net/Articles/951187/>
- <https://wiki.gentoo.org/wiki/RISC-V_ABIs>
- <https://gcc.gnu.org/onlinedocs/gcc/RISC-V-Options.html>

#### TV Encoder (TVE)

- clock source? PLL; must be 216 MHz

- test bars?

- <https://forum.armbian.com/topic/46922-orangepi-zero-2w-tv-out/>

- <https://forum.armbian.com/topic/6582-orange-pi-zero-h2h3-tv-out-on-mainline-working/>

- <https://github.com/robertojguerra/orangepi-zero-full-setup/blob/main/README2.md>

- <https://github.com/torvalds/linux/blob/master/drivers/gpu/drm/sun4i/sun4i_tv.c>

### Boot images

#### Tina Linux

- <https://github.com/paulwratt/mangopi-sbc-Tina-Linux> but the links
  are down
- `tina_d1-nezha_uart0_f133_nolcd.img`, burned with PhoenixCard (Work
  Type = Start up)
- result: **success**, console on UART0 (P3 pins 7 & 8) at 115200 baud

#### RT-Thread example

- <https://github.com/Cathy-lulu/MangoPi-Nezha-MQ>
- BOOT0, RT-Thread
- result: **partial success**, output on UART0 (P3 pin 7) at 500000
  baud, errors out late in boot process

#### mangopi-mq-riscv-2023-1-serial-console.img

- <https://github.com/ikruusa/mangopi-mq-riscv-images>
- U-Boot 2023.01-rc1, OpenSBI v1.3, Linux version 6.6.0-rc7
- result: **success**, console on UART3 (header not mounted by default)
  at 115200 baud

#### mq-r-f133-rtl8189fs-5113-dns-uart0.img

- from <https://mangopi.org/mangopi_mq>, but filename suggests it's for
  the MQ-R
- couldn't get it to work, no output on UART0 header
- **might have messed up the copy process**

### D1s bare-metal code

- [XFEL
  payloads](https://github.com/xboot/xfel/tree/master/payloads/d1_f133)
  - init for PLL etc.; `sdelay` function
  - examples of init & use of UART, SPI
  - DDR2 init (disassembled code)
- [D1 SPL](https://github.com/smaeul/sun20i_d1_spl)
  - drivers for many peripherals, including DRAM init in C
  - distilled version:
    <https://github.com/smaeul/u-boot/blob/d1-2022-10-31/drivers/ram/sunxi/mctl_hal-sun20iw1p1.c>
- what are these?
  <https://github.com/smaeul/sun20i_d1_spl/blob/mainline/drivers/dram/sun20iw1p1/lib-dram/t-head-compat.inc>
- [Assembly examples (blinky,
  GPIO)](https://steward-fu.github.io/website/mcu.htm#f133)
- [Xboot](https://steward-fu.github.io/website/mcu/f133/build_xboot.htm)
  -- not clear what is the point of it

### Related: Bare-metal code for D1-H (similar SoC)

- <https://github.com/bigmagic123/d1-nezha-baremeta>
  - a bunch of demos: UART, JTAG, vector instructions, timer, PLINT,
    watchdog
  - documentation is in Mandarin only
- <https://github.com/chaoyangnz/mpi-d1>
- <https://github.com/Ouyancheng/FlatHeadBro>
