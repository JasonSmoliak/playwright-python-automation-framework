def get_unique_usernames(usernames):

    return set(usernames)


def find_duplicate_values(values):

    seen = set()

    duplicates = set()

    for value in values:

        if value in seen:
            duplicates.add(value)

        seen.add(value)

    return duplicates
