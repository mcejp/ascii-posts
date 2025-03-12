---
layout: post
render_with_liquid: false
date: 2024-12-06
title: LVM
unlisted: true
---

## Move a single LV to a new PV

<https://unix.stackexchange.com/a/188854> one volume group solution

## Live-shrink FS & LV

Not possible with ext4:

    resize2fs: On-line shrinking not supported

## Should use entire disk or a single partition?

A: [Just use entire disk](https://serverfault.com/a/973769).
