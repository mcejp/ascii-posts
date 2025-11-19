---
layout: post
render_with_liquid: false
date: 2025-11-17
title: "Photoview minimalist setup with Podman"
unlisted: true
---

Photoview is a minimalist self-hosted photo gallery. You don't upload
any pictures through the Web UI -- they're taken straight from the file
system.

### Take 1: vanilla podman

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

### Take 2: systemd-managed container (Quadlet)

``` yaml
# ~/.config/containers/systemd/photoview.container

[Unit]
Description=photoview
Wants=network-online.target
After=network-online.target

[Container]
ContainerName=photoview
Image=docker.io/photoview/photoview:2
Environment=PHOTOVIEW_DATABASE_DRIVER=sqlite
Environment=PHOTOVIEW_SQLITE_PATH=/home/photoview/database/photoview.db
Environment=PHOTOVIEW_LISTEN_IP=::
PublishPort=8000:80
User=0
Volume=/etc/localtime:/etc/localtime:ro
Volume=/srv/photoview-data/database:/home/photoview/database
Volume=/srv/photoview-data/storage:/home/photoview/media-cache
Volume=/path/to/photos/on/host:/photos:ro

[Install]
WantedBy=multi-user.target
```

Notes

- assumes /srv/photoview-data is owned by user, not root
- if any volume path contains spaces, this will not work due to a bug in
  podman \<= 5.7 (<https://github.com/containers/podman/pull/27385>)
  - this only applies to the paths spelled out in the file; albums are
    subdirectories, so it's okay

TODO:

- auto-update
