from utils import with_input

with with_input(1) as file:
    data = file.read().splitlines()


def enumerate_values():
    value = 50
    for line in data:
        prev_value = value
        direction = line[0]
        steps = int(line[1:])
        value += steps if direction == "R" else -steps
        yield value, prev_value, direction
        value %= 100


part1 = sum(1 for value, _, _ in enumerate_values() if value % 100 == 0)
print(f"Part 1: {part1}")


def count_part2_zeroes(value, prev_value, direction):
    delta = 0
    if direction == "L":
        delta = 1 if value % 100 == 0 else -1 if prev_value == 0 else 0
    return abs(value // 100) + delta


part2 = sum(count_part2_zeroes(*args) for args in enumerate_values())
print(f"Part 2: {part2}")
