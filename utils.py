import sys
from contextlib import contextmanager


@contextmanager
def open_input(day: int):
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        filename = f"data/day{day}-test.txt"
    else:
        filename = f"data/day{day}.txt"
    with open(filename, "r") as file:
        yield file
