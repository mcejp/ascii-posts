---
layout: post
render_with_liquid: false
date: 2023-12-10
title: "ffmpeg"
unlisted: true
---

### Lossless

! <https://github.com/mifi/lossless-cut>

<https://superuser.com/a/522853> `-c:v libx264 -crf 0 -preset ultrafast`

### x11grab / Audio capture

    Audio encoding with ffmpeg
    17 Jul 2018 : investigation how to encode the java sound inside the CWE-774-TST5 test vistar ( on 05 Feb 2019 it was renamed to CSV-CCR-TST for the Juniper router tests):.

    Adding "-f alsa -i default" in the right place:

    ffmpeg -f x11grab -s 800x600 -i :0.0 -f alsa -i default -r 25 -vcodec libx264 -preset ultrafast -tune zerolatency -crf 18 -x264opts keyint=25:min-keyint=25:no-scenecut -f mpegts udp://multicast-bevtst:1234
    outputs an audio stream but without the sound made by the java program (or "speaker-test -t wav -c 2").

### Generate mp4 from C++

<https://github.com/ange-yaghi/direct-to-video>

### Rotate video (without re-encoding)

<https://stackoverflow.com/a/31683689>
