from utils import open_input


with open_input(7) as f:
    lines = f.read().splitlines()
    splitters = {
        y: {x for x, c in enumerate(line) if c == "^"} for y, line in enumerate(lines)
    }
    initial_beams = {lines[0].index("S")}

beams = initial_beams
splits = 0
for y in range(1, max(splitters) + 1):
    new_beams = set()
    for beam in beams:
        if beam in splitters[y]:
            splits += 1
            new_beams.add(beam - 1)
            new_beams.add(beam + 1)
        else:
            new_beams.add(beam)
    beams = new_beams

print(f"Part 1: {splits}")
