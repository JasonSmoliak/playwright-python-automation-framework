def all_tests_passed(results):

    return all(
        result == "PASSED"
        for result in results
    )


def any_test_failed(results):

    return any(
        result == "FAILED"
        for result in results
    )
