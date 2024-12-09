from itertools import cycle
from pathlib import Path

import numpy as np

module_path = Path(__file__).resolve().parent


def part_1(map):
    padded_map = np.ones([_ + 2 for _ in map.shape], dtype="<U1")
    padded_map[1:-1, 1:-1] = map
    i, j = [_.item() for _ in np.nonzero(padded_map == "^")]
    directions = cycle(["up", "right", "down", "left"])
    direction = next(directions)

    obstacles = padded_map == "#"
    points = []

    while True:
        if direction == "up":
            next_i = i - 1
            next_j = j
        elif direction == "right":
            next_i = i
            next_j = j + 1
        elif direction == "down":
            next_i = i + 1
            next_j = j
        elif direction == "left":
            next_i = i
            next_j = j - 1

        if padded_map[next_i, next_j] == "1":
            points.append((i, j))
            break

        if obstacles[next_i, next_j]:
            direction = next(directions)
        else:
            points.append((i, j))
            i = next_i
            j = next_j

    return len(set(points))


if __name__ == "__main__":
    with open(module_path / "input", "r") as file:
        data = file.read()
    map = np.array([[letter for letter in line] for line in data.splitlines()])
    solution = part_1(map)

    print("Advent of Code 2024 (day 6 - Python)")
    print(f"Solution for part 1: {solution}")
