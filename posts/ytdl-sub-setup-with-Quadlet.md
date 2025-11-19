---
layout: post
render_with_liquid: false
date: 2025-11-17
title: "ytdl-sub setup with Quadlet"
unlisted: true
---

The container uses a supervisor which really wants to be PID 0 (at least
internally), while ytdl-sub itself runs as whatever `$PUID:$PGID` are
set to (911 by default).

Okay, so we need a root inside, but can it be *nobody* (65534) on the
outside? Yes, that seems to work.

``` yaml
# /etc/systemd/system/ytdl-sub.service

[Unit]
Description=ytdl-sub
Wants=network-online.target
After=network-online.target

[Container]
ContainerName=ytdl-sub
Image=ghcr.io/jmbannon/ytdl-sub:latest
Environment="CRON_SCHEDULE=30 4 * * *"
Environment=CRON_RUN_ON_START=false
Environment=PUID=1000
Environment=PGID=1000
Environment=TZ=Etc/UTC  # <-- adapt to your needs
PodmanArgs=--uidmap 0:65534:1 --uidmap 1000:1000:1 --gidmap 0:65534:1 --gidmap 1000:1000:1
Volume=/srv/ytdl-sub/config:/config
Volume=/media/nas/public/Video:/Video

[Install]
WantedBy=multi-user.target
```

TODO:

- auto-update
- try to run this as a real rootless container
