from dataclasses import dataclass


@dataclass
class PostPayload:
    title: str
    body: str
    user_id: int
