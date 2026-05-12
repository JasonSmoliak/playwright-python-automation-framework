def sort_usernames(usernames):

    return sorted(usernames)


def sort_users_by_age(users):

    return sorted(
        users,
        key=lambda user: user["age"]
    )
