import pulp

from utils import open_input


def compute_bitmask(nums: list[int], length: int):
    bitmask = 0
    for num in nums:
        bitmask |= 1 << (length - num - 1)
    return bitmask


def parse_line(line: str):
    """[####] (2,3) (0,3) (1,3) (0,1,3) {34,24,10,51}"""
    light, *buttons, joltages = line.split()
    joltages = list(map(int, joltages[1:-1].split(",")))
    light_bits = [int(c == "#") for c in light[1:-1]]
    light = sum(
        light_bits[i] * 2 ** (len(light_bits) - i - 1) for i in range(len(light_bits))
    )
    buttons = [list(map(int, button[1:-1].split(","))) for button in buttons]
    button_bitmasks = [compute_bitmask(button, len(light_bits)) for button in buttons]
    return light, buttons, button_bitmasks, joltages


with open_input(10) as file:
    data = [parse_line(line) for line in file.read().splitlines()]


def find_minimum_pushes(light: int, buttons: list[int]):
    states = {0}
    steps = 0
    while light not in states:
        states = {state ^ button for state in states for button in buttons}
        steps += 1
    return steps


part1 = sum(find_minimum_pushes(light, bitmasks) for light, _, bitmasks, _ in data)
print(f"Part 1: {part1}")


def find_minimum_joltage_pushes(buttons: list[list[int]], joltages: list[int]):
    button_vectors = [
        tuple(int(i in button) for i in range(len(joltages))) for button in buttons
    ]
    x = [
        pulp.LpVariable(f"x{i}", lowBound=0, cat="Integer") for i in range(len(buttons))
    ]
    prob = pulp.LpProblem("JoltagePushes", pulp.LpMinimize)
    prob += pulp.lpSum(x)
    for j in range(len(joltages)):
        prob += (
            pulp.lpSum(x[i] * button_vectors[i][j] for i in range(len(buttons)))
            == joltages[j]
        )
    prob.solve(pulp.PULP_CBC_CMD(msg=0))

    return int(pulp.value(prob.objective))


part2 = sum(
    find_minimum_joltage_pushes(buttons, joltages) for _, buttons, _, joltages in data
)
print(f"Part 2: {part2}")
