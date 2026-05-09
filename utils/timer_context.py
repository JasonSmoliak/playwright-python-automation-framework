import time


class TimerContext:
    def __enter__(self):
        self.start = time.time()

        print("\nStarting timer...")

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        end = time.time()

        execution_time = round(end - self.start, 2)

        print(
            f"Execution completed in "
            f"{execution_time} seconds"
        )
