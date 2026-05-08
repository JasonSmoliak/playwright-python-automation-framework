import time
import uuid


def unique_string(prefix="test"):
    timestamp = int(time.time())
    short_uuid = uuid.uuid4().hex[:6]

    return f"{prefix}_{timestamp}_{short_uuid}"


def unique_post_payload():
    unique_id = unique_string("post")

    return {
        "title": f"{unique_id}_title",
        "body": f"{unique_id}_body",
        "userId": 1,
    }
