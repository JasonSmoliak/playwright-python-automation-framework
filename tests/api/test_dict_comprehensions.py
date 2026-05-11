import pytest

from utils.dict_comprehension_examples import (
    extract_active_users,
    remove_none_values,
)

pytestmark = pytest.mark.api


def test_dict_comprehensions():

    users = [
        {
            "username": "jay",
            "role": "admin",
            "active": True,
        },
        {
            "username": "sarah",
            "role": "viewer",
            "active": False,
        },
        {
            "username": "mike",
            "role": "editor",
            "active": True,
        },
    ]

    active_users = extract_active_users(users)

    payload = {
        "title": "Playwright Test",
        "body": None,
        "userId": 1,
    }

    cleaned_payload = remove_none_values(payload)

    print(active_users)
    print(cleaned_payload)

    assert active_users == {
        "jay": "admin",
        "mike": "editor",
    }

    assert cleaned_payload == {
        "title": "Playwright Test",
        "userId": 1,
    }
