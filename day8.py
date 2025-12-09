from utils import open_input


with open_input(8) as f:
    points = [tuple(map(int, line.split(","))) for line in f.read().splitlines()]

MAX_POINTS = 10 if len(points) == 20 else 1000


def get_distance(p1, p2) -> int:
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2) ** 0.5


distances = [
    (get_distance(points[i], points[j]), (points[i], points[j]))
    for i in range(len(points))
    for j in range(i + 1, len(points))
]

pairs = [pair for _, pair in sorted(distances, key=lambda x: x[0])]


def process_pair(pair, junctions):
    junction_a = next((j for j in junctions if pair[0] in j))
    junction_b = next((j for j in junctions if pair[1] in j))
    if junction_a is not junction_b:
        junctions.append(junction_a | junction_b)
        junctions.remove(junction_a)
        junctions.remove(junction_b)


junctions = [{p} for p in points]
for pair in pairs[:MAX_POINTS]:
    process_pair(pair, junctions)

lengths = sorted([len(j) for j in junctions], reverse=True)[:3]
print(f"Part 1: {lengths[0] * lengths[1] * lengths[2]}")

for pair in pairs[MAX_POINTS:]:
    process_pair(pair, junctions)
    if len(junctions) == 1:
        break
print(f"Part 2: {pair[0][0] * pair[1][0]}")
