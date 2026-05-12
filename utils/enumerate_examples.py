def format_test_steps(steps):

    return [
        f"Step {index}: {step}"
        for index, step in enumerate(steps, start=1)
    ]


def find_failed_tests(results):

    return [
        index
        for index, result in enumerate(results, start=1)
        if result == "FAILED"
    ]
