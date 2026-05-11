def get_active_users(users):

    return [
        user["username"]
        for user in users
        if user["active"]
    ]


def generate_test_emails(count):

    return [
        f"qa_user_{n}@example.com"
        for n in range(count)
    ]
