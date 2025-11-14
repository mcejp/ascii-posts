---
layout: post
render_with_liquid: false
date: 2025-11-08
title: "Photoview minimalist setup with Podman"
unlisted: true
---

Photoview is a minimalist self-hosted photo gallery. You don't upload
any pictures through the Web UI -- they're taken straight from the file
system.

### The script

This assumes **rootless Podman**, so `--user 0` inside the container
will resolve the **current user** on host.

On Fedora it was necessary to listen on `::` rather than `0.0.0.0`.
Probably has to do with the new networking agent in Podman.

``` sh
mkdir -p photoview-data/{database,storage}

podman run -it --rm --name photoview --user 0 \
        -p 8000:80
        -e PHOTOVIEW_DATABASE_DRIVER=sqlite \
        -e PHOTOVIEW_LISTEN_IP=:: \
        -e PHOTOVIEW_SQLITE_PATH=/home/photoview/database/photoview.db \
        -v /etc/localtime:/etc/localtime:ro \
        -v ./photoview-data/database:/home/photoview/database \
        -v ./photoview-data/storage:/home/photoview/media-cache \
        -v /path/to/photos/on/host:/photos:ro \
        photoview/photoview:2
```
