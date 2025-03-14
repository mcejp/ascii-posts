import argparse
import datetime
from pathlib import Path
from subprocess import check_call, check_output
from textwrap import dedent
import tomllib

import requests
from requests.models import PreparedRequest


class JoplinClient:
    def __init__(self, port, token):
        self._base_url = f"http://localhost:{port}"
        self._token = token

    def get(self, url, params={}):
        req = PreparedRequest()
        req.prepare_url(self._base_url + url, params | dict(token=self._token))
        return requests.get(req.url).json()


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

types = [dict(suffix="", delimiters=True), dict(suffix=":full", delimiters=False)]
index = []

for type in types:
    # first we need to find the tag by name to get its ID
    tags = client.get("/search", params=dict(query=config["publish_tag"] + type["suffix"], type="tag"))
    assert tags["has_more"] is False
    (tag_info,) = tags["items"]

    # find posts
    notes = client.get(
        f"/tags/{tag_info['id']}/notes",
        params=dict(fields="body,id,title,user_updated_time"),
    )
    # print(json.dumps(notes, indent=2))
    assert notes["has_more"] is False

    # build post list
    # TODO: sort by timestamp
    def format_date(timestamp): return datetime.datetime.fromtimestamp(timestamp / 1000).date().isoformat()

    # export markdown & parse
    for note in notes["items"]:
        # import json; print(json.dumps(note, indent=2))

        note_tags = client.get(f"/notes/{note['id']}/tags")

        if type["delimiters"]:
            lines: list[str] = note["body"].split("\n")

            begin_line = lines.index("### PUBLISHED PART")
            end_line = lines.index("### UNPUBLISHED PART")
            assert end_line > begin_line

            post = "\n".join(lines[begin_line + 1 : end_line])
        else:
            post = note["body"]

        # post = post.replace("<ascii-posts:post-list/>", post_list_md)

        #post = post.replace(" -- ", "&mdash;")          # this breaks commands in PDF topic

        # slug-ify filename
        def slugify(filename: str):
            filename = filename.replace(" ", "-")
            filename = filename.replace("/", "-")
            return filename
    
        filename = slugify(note["title"])

        assert "/" not in filename
        assert "\\" not in filename
        assert filename not in {"", ".", ".."}

        # Necessary in order to linkify URLs
        post = check_output(["pandoc", "-f", "gfm", "-t", "gfm"],
                            input=post.strip(),
                            text=True)

        note["filename"] = filename
        index.append(dict(title=note['title'],
                          tags=[tag["title"] for tag in note_tags["items"]],
                          url=f"posts/{note['filename']}.html",
                          user_updated_time=note['user_updated_time']))

        with open(out_dir / f"{filename}.md", "wt") as f:
            f.write(dedent(f"""\
            ---
            layout: post
            render_with_liquid: false
            date: {format_date(note['user_updated_time'])}
            title: {note["title"]}
            unlisted: true
            ---

            """))
            f.write(post.strip())
            f.write("\n")


def decorated_title(note):
    if "starred_tag" in config and config["starred_tag"] in note["tags"]:
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
        f.write(f"|[{decorated_title(note)}]({note['url']})|{format_date(note['user_updated_time'])}|\n")

check_call("git add -A", shell=True, cwd=out_dir)
check_call("git commit -m Update", shell=True, cwd=out_dir)
