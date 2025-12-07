from itertools import zip_longest
from operator import add, mul
from functools import reduce
from utils import open_input


with open_input(6) as f:
    lines = f.read().splitlines()
    group_lengths = [len(v) for v in (lines[-1][1:] + " ").replace("*", "+").split("+")]
    inputs = [[] for _ in group_lengths]
    for line in lines[:-1]:
        index = 0
        for col, length in enumerate(group_lengths):
            inputs[col].append(line[index : index + length])
            index += length + 1


def solve(func):
    return sum(
        reduce(add if op == "+" else mul, func(values), 0 if op == "+" else 1)
        for values, op in zip(inputs, lines[-1].split())
    )


def get_numbers(values):
    return [int("".join(v for v in vs if v != " ")) for vs in zip_longest(*values)]


print(f"Part 1: {solve(lambda x: list(map(int, x)))}")
print(f"Part 2: {solve(get_numbers)}")
