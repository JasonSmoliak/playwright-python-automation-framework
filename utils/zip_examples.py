def compare_test_results(expected, actual):

    return [
        expected_result == actual_result
        for expected_result, actual_result
        in zip(expected, actual)
    ]


def pair_users_and_roles(users, roles):

    return [
        f"{user} -> {role}"
        for user, role in zip(users, roles)
    ]
