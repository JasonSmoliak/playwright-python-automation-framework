from collections import defaultdict


def group_users_by_role(users):

    grouped = defaultdict(list)

    for user in users:

        grouped[user["role"]].append(
            user["username"]
        )

    return grouped


def group_test_results(results):

    grouped = defaultdict(list)

    for test_name, status in results:

        grouped[status].append(test_name)

    return grouped
