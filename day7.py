from collections import defaultdict
from utils import open_input


with open_input(7) as f:
    lines = f.read().splitlines()
    splitters = {
        y: {x for x, c in enumerate(line) if c == "^"} for y, line in enumerate(lines)
    }
    initial_beam = lines[0].index("S")

beams_count = defaultdict(int, {initial_beam: 1})
splits = 0
possibilities = 1
for y in range(1, max(splitters) + 1):
    new_beams = beams_count.copy()
    for beam, count in beams_count.items():
        if beam in splitters[y] and count > 0:
            splits += 1
            possibilities += count
            new_beams[beam - 1] += count
            new_beams[beam + 1] += count
            new_beams[beam] -= count
    beams_count = new_beams

print(f"Part 1: {splits}")
print(f"Part 2: {possibilities}")
