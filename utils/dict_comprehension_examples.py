def extract_active_users(users):

    return {
        user["username"]: user["role"]
        for user in users
        if user["active"]
    }


def remove_none_values(payload):

    return {
        key: value
        for key, value in payload.items()
        if value is not None
    }
