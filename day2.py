import math
from utils import open_input

with open_input(2) as file:
    ranges = [tuple(map(int, line.split("-"))) for line in file.read().split(",")]


def has_same_parts(number: int):
    dividor = 10 ** (math.ceil(math.log10(number)) // 2)
    return number // dividor == number % dividor


def has_similar_parts(number: int):
    parts = str(number)
    for i in range(1, len(parts) // 2 + 1):
        part = parts[:i]
        for j in range(i, len(parts), i):
            if parts[j : j + i] != part:
                break
        else:
            return True
    return False


def solve(predicate):
    return sum(
        number for a, b in ranges for number in range(a, b + 1) if predicate(number)
    )


print(f"Part 1: {solve(has_same_parts)}")
print(f"Part 2: {solve(has_similar_parts)}")
