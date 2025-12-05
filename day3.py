from utils import open_input


with open_input(3) as file:
    battery_sets = [list(map(int, line)) for line in file.read().splitlines()]


def get_joltage(batteries: list[int], batteries_count: int):
    result = 0
    for i in range(batteries_count):
        digit = max(batteries[: len(batteries) - (batteries_count - i - 1)])
        batteries = batteries[batteries.index(digit) + 1 :]
        result = result * 10 + digit
    return result


print(f"Part 1: {sum(get_joltage(batteries, 2) for batteries in battery_sets)}")
print(f"Part 2: {sum(get_joltage(batteries, 12) for batteries in battery_sets)}")
