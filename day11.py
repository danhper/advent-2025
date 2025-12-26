from utils import open_input


nodes = {}
with open_input(11) as file:
    for line in file:
        s, e = line.split(":")
        nodes[s] = e.strip().split(" ")


def find_paths(node: str, paths: dict[str, list[list[str]]]):
    if node == "out":
        return [[node]]
    if node in paths:
        return paths[node]
    paths[node] = [
        path + [node]
        for next_node in nodes[node]
        for path in find_paths(next_node, paths)
    ]
    return paths[node]


paths_you = find_paths("you", {})

print("Part 1:", len(paths_you))

paths_svr = find_paths("svr", {})

print("Part 2:", sum(1 for p in paths_svr if "fft" in p and "dac" in p))
