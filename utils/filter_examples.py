def get_failed_tests(results):

    return list(
        filter(
            lambda result: result == "FAILED",
            results,
        )
    )


def get_active_users(users):

    return list(
        filter(
            lambda user: user["active"],
            users,
        )
    )
