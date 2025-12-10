import random
from utils import open_input


with open_input(9) as f:
    points = [tuple(map(int, line.split(","))) for line in f.read().splitlines()]


def get_distance(p1, p2) -> int:
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def get_area(p1, p2) -> int:
    width = abs(p1[0] - p2[0]) + 1
    height = abs(p1[1] - p2[1]) + 1
    return width * height


max_area = 0
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        area = get_area(points[i], points[j])
        if area > max_area:
            max_area = area

print(f"Part 1: {max_area}")


def is_in_polygon(point, polygon) -> bool:
    # TODO: Implement this
    return True


max_area = 0
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        area = get_area(points[i], points[j])
        if area <= max_area:
            continue
        rectangle_corners = [
            (min(points[i][0], points[j][0]), min(points[i][1], points[j][1])),
            (max(points[i][0], points[j][0]), min(points[i][1], points[j][1])),
            (max(points[i][0], points[j][0]), max(points[i][1], points[j][1])),
            (min(points[i][0], points[j][0]), max(points[i][1], points[j][1])),
        ]
        to_check = [p for p in rectangle_corners if p != points[i] and p != points[j]]
        if all(is_in_polygon(p, points) for p in rectangle_corners):
            max_area = area


print(f"Part 2: {max_area}")
