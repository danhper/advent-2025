from utils import open_input


with open_input(5) as f:
    lines = f.read().splitlines()

separator = lines.index("")
ranges = [tuple(map(int, line.split("-"))) for line in lines[:separator]]
ingredients = [int(line) for line in lines[separator + 1 :]]

part1 = sum(1 for ingr in ingredients if any(a <= ingr <= b for a, b in ranges))
print(f"Part 1: {part1}")


def merge_ranges(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    ranges.sort(key=lambda x: x[0])
    merged_ranges = [ranges[0]]
    for a, b in ranges[1:]:
        va, vb = merged_ranges[-1]
        if a > vb:
            merged_ranges.append((a, b))
        else:
            merged_ranges[-1] = (va, max(vb, b))
    return merged_ranges


part2 = sum(b - a + 1 for a, b in merge_ranges(ranges))
print(f"Part 2: {part2}")
