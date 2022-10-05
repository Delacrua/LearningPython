from contextlib import contextmanager
from timeit import default_timer


@contextmanager
def timer():
    time_start = default_timer()
    yield lambda: time_end - time_start
    time_end = default_timer()


if __name__ == "__main__":
    with timer() as t:
        print(sum(range(1_000_000)))
    print(t())

    with timer() as t2:
        print(sum(range(1_000)))
    print(t2())
