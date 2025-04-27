import argparse
import datetime
from pathlib import Path
from subprocess import check_call, check_output
from textwrap import dedent
import tomllib
import traceback

from asciiposts import JoplinClient, get_filtered_notes


parser = argparse.ArgumentParser()
parser.add_argument("out_dir", type=Path)
args = parser.parse_args()

with open("config.toml", "rb") as f:
    config = tomllib.load(f)

out_dir = args.out_dir
client = JoplinClient(port=config["port"], token=config["token"])

# clean output directory (we always rebuild the entire tree)
for path in out_dir.iterdir():
    if path.name == ".git":
        continue

    path.unlink()

"""
we have 2 types (sets) of notes:
- notes that contain a published part and a non-published part
- notes that are published in full
"""

index = []

# build post list
# TODO: sort by timestamp
for type, note in get_filtered_notes(client, publish_tag=config["publish_tag"]):
    # import json; print(json.dumps(note, indent=2))

    note_tags = [tag["title"] for tag in client.get(f"/notes/{note['id']}/tags")["items"]]

    try:
        if type["delimiters"]:
            lines: list[str] = note["body"].split("\n")

            begin_line = lines.index("### PUBLISHED PART")
            end_line = lines.index("### UNPUBLISHED PART")
            assert end_line > begin_line

            post = "\n".join(lines[begin_line + 1 : end_line])
        else:
            post = note["body"]

            assert "### PUBLISHED PART" not in post
            assert "### UNPUBLISHED PART" not in post
    except Exception:
        print(f'error processing note "{note["title"]}":')
        traceback.print_exc()

    # post = post.replace("<ascii-posts:post-list/>", post_list_md)

    #post = post.replace(" -- ", "&mdash;")          # this breaks commands in PDF topic

    # slug-ify file name
    def slugify(filename: str):
        filename = filename.replace(" ", "-")
        filename = filename.replace("/", "-")
        filename = filename.replace(":", "-")
        while "--" in filename:
            filename = filename.replace("--", "-")  # just because it's nicer
        while filename.endswith("."):
            filename = filename[:-1]
        return filename

    def format_date(timestamp):
        return datetime.datetime.fromtimestamp(timestamp / 1000).date().isoformat()

    filename = slugify(note["title"])

    assert "/" not in filename
    assert "\\" not in filename
    assert filename not in {"", ".", ".."}

    # Necessary in order to linkify URLs
    post = check_output(["pandoc", "-f", "gfm", "-t", "gfm"],
                        input=post.strip(),
                        text=True)

    index.append(dict(title=note['title'],
                      tags=note_tags,
                      starred="starred_tag" in config and config["starred_tag"] in note_tags,
                      url=f"posts/{filename}.html",
                      user_updated_time=note['user_updated_time']))

    with open(out_dir / f"{filename}.md", "wt") as f:
        f.write(dedent(f"""\
            ---
            layout: post
            render_with_liquid: false
            date: {format_date(note['user_updated_time'])}
            title: "{note["title"].replace('"', '\\"')}"
            unlisted: true
            ---

            """))
        f.write(post.strip())
        f.write("\n")


def decorated_title(note):
    if note["starred"]:
        return "&#x2B50; " + note["title"]
    else:
        return note["title"]


with open(out_dir / f"../index.md", "wt") as f:
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

check_call("git add -A", shell=True, cwd=out_dir)
check_call("git commit -m Update", shell=True, cwd=out_dir)
