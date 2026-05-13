def normalize_usernames(usernames):

    return list(
        map(
            lambda username: username.lower(),
            usernames,
        )
    )


def convert_prices_to_float(prices):

    return list(
        map(
            lambda price: float(
                price.replace("$", "")
            ),
            prices,
        )
    )
