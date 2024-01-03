from pathlib import Path
from subprocess import check_call
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


with open("config.toml", "rb") as f:
    config = tomllib.load(f)

out_dir = Path("out")
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

for type in types:
    # first we need to find the tag by name to get its ID
    tags = client.get("/search", params=dict(query=config["tag_name"] + type["suffix"], type="tag"))
    assert tags["has_more"] is False
    (tag_info,) = tags["items"]

    # find posts
    notes = client.get(
        f"/tags/{tag_info['id']}/notes",
        params=dict(fields="body,id,title,updated_time"),
    )
    # print(json.dumps(notes, indent=2))
    assert notes["has_more"] is False

    # build post list
    # TODO: sort by timestamp
    # def format_date(timestamp): return datetime.datetime.fromtimestamp(timestamp / 1000).date().isoformat()
    # post_list_md = "\n".join(f"- {note['title']} (updated {format_date(note['updated_time'])})" for note in notes["items"])

    # export markdown & parse
    for note in notes["items"]:
        # print(json.dumps(note, indent=2))

        if type["delimiters"]:
            lines: list[str] = note["body"].split("\n")

            begin_line = lines.index("### PUBLISHED PART")
            end_line = lines.index("### UNPUBLISHED PART")
            assert end_line > begin_line

            post = "\n".join(lines[begin_line + 1 : end_line])
        else:
            post = note["body"]

        # post = post.replace("<ascii-posts:post-list/>", post_list_md)

        filename = note["title"].replace("/", "\u29F8")  # use alternative slash in file name

        assert "/" not in filename
        assert "\\" not in filename

        with open(out_dir / f"{filename}.md", "wt") as f:
            f.write(post.strip() + "\n")

check_call("git add -A", shell=True, cwd=out_dir)
check_call("git commit -m Update", shell=True, cwd=out_dir)
