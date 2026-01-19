import argparse
import datetime
from pathlib import Path
import re
from subprocess import check_call, check_output
from textwrap import dedent
import tomllib
import traceback

from asciiposts import JoplinClient, get_filtered_notes


def format_date(timestamp):
    """Convert Joplin timestamp (ms) to ISO date string."""
    return datetime.datetime.fromtimestamp(timestamp / 1000).date().isoformat()


def slugify(filename: str):
    """Convert a note title to a URL-safe filename slug."""
    filename = filename.replace(" ", "-")
    filename = filename.replace("/", "-")
    filename = filename.replace(":", "-")
    filename = filename.replace("?", "-")
    while "--" in filename:
        filename = filename.replace("--", "-")  # just because it's nicer
    while filename.endswith("."):
        filename = filename[:-1]

    assert "/" not in filename
    assert "\\" not in filename
    assert filename not in {"", ".", ".."}

    return filename


parser = argparse.ArgumentParser()
parser.add_argument("--commit", default=False, action="store_true")
parser.add_argument("out_dir", type=Path)
args = parser.parse_args()

with open("config.toml", "rb") as f:
    config = tomllib.load(f)

out_dir = args.out_dir
client = JoplinClient(port=config["port"], token=config["token"])

# Squash previous history into a single commit
# check_call("git update-ref -d refs/heads/site", shell=True, cwd=out_dir)
# check_call("git checkout --orphan site", shell=True, cwd=out_dir)
# check_call("git add -A", shell=True, cwd=out_dir)
# check_call("git commit -m 'Generate site'", shell=True, cwd=out_dir)

# clean output directory (we always rebuild the entire tree)
for path in (out_dir / "posts").iterdir():
    if path.name == ".git":
        continue

    path.unlink()

"""
we have 2 types (sets) of notes:
- notes that contain a published part and a non-published part
- notes that are published in full
"""

# Pre-fetch all notes and build ID => slug mapping for internal link resolution
all_notes = list(get_filtered_notes(client, publish_tag=config["publish_tag"]))
note_id_to_slug = {note["id"]: slugify(note["title"]) for _, note in all_notes}

index = []

# build post list
# TODO: sort by timestamp
for type, note in all_notes:
    # import json; print(json.dumps(note, indent=2))

    note_tags = [tag["title"] for tag in client.get(f"/notes/{note['id']}/tags")["items"]]

    try:
        if type["delimiters"]:
            lines: list[str] = note["body"].split("\n")

            # Support any heading level (# to ######) for delimiters
            begin_line = next(i for i, line in enumerate(lines) if re.match(r'^#{1,6}\s+PUBLISHED PART\s*$', line.strip()))
            end_line = next(i for i, line in enumerate(lines) if re.match(r'^#{1,6}\s+UNPUBLISHED PART\s*$', line.strip()))
            assert end_line > begin_line

            post = "\n".join(lines[begin_line + 1 : end_line])
        else:
            post = note["body"]

            # Ensure no delimiter headings exist in non-delimited posts
            assert not any(re.match(r'^#{1,6}\s+PUBLISHED PART\s*$', line.strip()) for line in post.split("\n"))
            assert not any(re.match(r'^#{1,6}\s+UNPUBLISHED PART\s*$', line.strip()) for line in post.split("\n"))
    except Exception:
        print(f'error processing note "{note["title"]}":')
        traceback.print_exc()
        continue

    # post = post.replace("<ascii-posts:post-list/>", post_list_md)

    #post = post.replace(" -- ", "&mdash;")          # this breaks commands in PDF topic

    # Process images in the post content    
    pattern = r'!\[(.*?)\]\(:/([a-f0-9]{32})\)'
    
    def replace_image(match):
        caption, resource_id = match.groups()

        resource = client.get(f"/resources/{resource_id}")
        resource_bytes = client.get_resource_file(resource_id)

        # Create a filename that includes the original name if available
        filename = resource.get("title", resource_id)
        if not filename.endswith((".png", ".jpg", ".jpeg", ".gif")):
            filename = f"{filename}.{resource['file_extension']}"

        # Save the file
        image_path = out_dir / "images" / filename
        image_path.write_bytes(resource_bytes)

        # Return the new markdown image reference
        return f"![{caption}](../images/{filename})"

    post = re.sub(pattern, replace_image, post)

    # Process internal note links: [text](:/note_id) => [text](slug.html)
    link_pattern = r'(?<!!)\[(.*?)\]\(:/([a-f0-9]{32})\)'

    def replace_internal_link(match):
        link_text, target_note_id = match.groups()

        if target_note_id in note_id_to_slug:
            target_slug = note_id_to_slug[target_note_id]
            return f"[&#x1f4dd; {link_text}]({target_slug}.html)"
        else:
            print(f'  Warning: Link to unpublished note {target_note_id} in "{note["title"]}"')
            return link_text  # Strip link, keep text

    post = re.sub(link_pattern, replace_internal_link, post)

    filename = note_id_to_slug[note["id"]]

    # Necessary in order to linkify URLs
    post = check_output(["pandoc", "-f", "gfm", "-t", "gfm"],
                        input=post.strip(),
                        text=True)

    index.append(dict(title=note['title'],
                      tags=note_tags,
                      starred="starred_tag" in config and config["starred_tag"] in note_tags,
                      url=f"posts/{filename}.html",
                      user_updated_time=note['user_updated_time']))

    with open(out_dir / "posts" / f"{filename}.md", "wt") as f:
        f.write(dedent(f"""\
            ---
            layout: post
            render_with_liquid: false
            date: {format_date(note['user_updated_time'])}
            title: "{note["title"].replace('"', '\\"')}"
            unlisted: true
            ---

            """))
        f.write(post.rstrip())
        f.write("\n")


def decorated_title(note):
    if note["starred"]:
        return "&#x2B50; " + note["title"]
    else:
        return note["title"]


with open(out_dir / "index.md", "wt") as f:
    f.write(dedent(f"""\
        ---
        layout: default
        ---

        _ASCII Posts_ are snippets extracted from my personal knowledge base and updated periodically.
        They are published in the hope that they may be of use to someone, without requiring the effort of a polished blog article on my part.
        As such, there is absolutely no guarantee of accuracy or completeness :)

        [Read more...](posts/ASCII-Posts.html)

        |Title|Last updated|
        |-----|------------|
        """))
    for note in sorted(index, key=lambda note: note['user_updated_time'], reverse=True):
        if note["starred"]:
            f.write(f"|[{decorated_title(note)}]({note['url']})|{format_date(note['user_updated_time'])}|\n")
    for note in sorted(index, key=lambda note: note['user_updated_time'], reverse=True):
        if not note["starred"]:
            f.write(f"|[{decorated_title(note)}]({note['url']})|{format_date(note['user_updated_time'])}|\n")

if args.commit:
    check_call("git add -A", shell=True, cwd=out_dir)
    check_call("git commit -m Update", shell=True, cwd=out_dir)
