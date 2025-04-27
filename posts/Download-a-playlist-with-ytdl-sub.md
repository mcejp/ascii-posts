---
layout: post
render_with_liquid: false
date: 2024-09-23
title: "Download a playlist with ytdl-sub"
unlisted: true
---

(Assuming Jellyfin as the media player)

### config.yml

``` yaml
...

presets:
  episode_by_playlist_index:
    overrides:
      # a single season
      season_number: "1"
      season_number_padded: "01"
      # this will break if the playlist is re-ordered...
      episode_number: "{playlist_index}"
      episode_number_padded: "{playlist_index_padded}"
      # do not include upload date in episode title
      episode_title: "{title}"
```

### subscriptions.yml

``` yaml
"Jellyfin TV Show by Date | episode_by_playlist_index | best_video_quality":
  "Bendix Central Air Data Computer": "https://www.youtube.com/playlist?list=PL-_93BVApb59k-GD2e83E6prrhm5fobtV"
```
