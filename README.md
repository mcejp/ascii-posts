Intro: [ASCII Posts](https://notes.mcejp.com/posts/ASCII-Posts.html)

Prerequisities:
- Joplin with Web Clipper server enabled
- `requests` Python package
- Git

### config.toml

```toml
port = 41184
publish_tag = "publish"
starred_tag = "starred"
token = "YOUR JOPLIN WEB CLIPPER TOKEN"
```

### TODO

- Align Jekyll versions between Gemfile and Docker image (currently using jekyll/jekyll:4.2.2 which only goes up to 4.2.x)

### Bugs

- Editing the unpublished part of a note changes the modification date of the published note
