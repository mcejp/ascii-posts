---
layout: post
render_with_liquid: false
date: 2025-09-22
title: "CRON jobs logging & monitoring"
unlisted: true
---

#### Where to find CRON logs?

Start with `journalctl --unit crond -n all`.

But in general, it is a mess. The correct solution seems to be piping
command output to the system journal within the cron script. Don't
forget to redirect stderr. Example that does both:

    systemd-cat -t example ./do-the-work.sh

(then `journalctl -t example`)

### Health monitoring (dead man's switch)

- <https://healthchecks.io> (20 monitors in free tier)
- <https://cronitor.io> (5 monitors in free tier)
