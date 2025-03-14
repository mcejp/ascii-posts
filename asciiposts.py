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


# Not really generic, so not part of JoplinClient
def get_filtered_notes(client: JoplinClient, publish_tag: str):
    """
    we have 2 types (sets) of notes:
    - notes that contain a published part and a non-published part
    - notes that are published in full
    """
    TYPES = [dict(suffix="", delimiters=True),
             dict(suffix=":full", delimiters=False)]

    for type in TYPES:
        # first we need to find the tag by name to get its ID
        tags = client.get(
            "/search", params=dict(query=publish_tag + type["suffix"], type="tag")
        )
        assert tags["has_more"] is False

        # should never yield more than 1 result in practice
        for tag_info in tags["items"]:
            # find posts
            notes = client.get(
                f"/tags/{tag_info['id']}/notes",
                params=dict(fields="body,id,title,user_updated_time"),
            )
            # print(json.dumps(notes, indent=2))
            assert notes["has_more"] is False

            for note in notes["items"]:
                yield (type, note)
