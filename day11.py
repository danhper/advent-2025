from collections import defaultdict
from utils import open_input


nodes = {}
with open_input(11) as file:
    for line in file:
        s, e = line.split(":")
        nodes[s] = e.strip().split(" ")

queue = ["you"]
counts = defaultdict(int)
while queue:
    current = queue.pop(0)
    for node in nodes[current]:
        if node == "out":
            counts[current] += 1
        elif node in counts:
            counts[current] += counts[node]
        if node != "out":
            queue.append(node)


print("Part 1:", sum(counts.values()))
