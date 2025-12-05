from utils import open_input


with open_input(4) as f:
    rolls = {(x, y) for y, line in enumerate(f) for x, c in enumerate(line) if c == "@"}


def count_neighbors(x: int, y: int):
    deltas = {(dx, dy) for dx in [-1, 0, 1] for dy in [-1, 0, 1]} - {(0, 0)}
    return sum(1 for dx, dy in deltas if (x + dx, y + dy) in rolls)


part1 = sum(1 for x, y in rolls if count_neighbors(x, y) < 4)
print(f"Part 1: {part1}")

rolls_count = len(rolls)
while to_remove := {(x, y) for x, y in rolls if count_neighbors(x, y) < 4}:
    rolls -= to_remove
print(f"Part 2: {rolls_count - len(rolls)}")
