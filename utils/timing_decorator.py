import time


def measure_execution_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()

        execution_time = round(end - start, 2)

        print(
            f"\nExecution time for "
            f"{func.__name__}: "
            f"{execution_time} seconds"
        )

        return result

    return wrapper
