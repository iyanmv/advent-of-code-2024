from pathlib import Path

import numpy as np
import networkx as nx

module_path = Path(__file__).resolve().parent


def count_paths(position, hiking_map):
    x, y = position
    value = hiking_map[x, y]

    if value == 9:
        return 1

    possible_next_positions = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
    next_positions = []

    for x_next, y_next in possible_next_positions:
        if hiking_map[x_next, y_next] == value + 1:
            next_positions.append((x_next, y_next))

    if len(next_positions) == 0:
        return 0

    count = 0
    for pos in next_positions:
        count += count_paths(pos, hiking_map)

    return count


def part_2(hiking_map):
    rows, cols = hiking_map.shape
    padded_map = -1 * np.ones((rows + 2, cols + 2), dtype=int)
    padded_map[1:-1, 1:-1] = hiking_map
    trailheads = np.argwhere(padded_map == 0)

    ratings = []
    for trailhead in trailheads:
        ratings.append(count_paths(trailhead, padded_map))

    return sum(ratings)


if __name__ == "__main__":
    with open(module_path / "input", "r") as file:
        hiking_map = np.array(
            [[n for n in line] for line in file.read().splitlines()], dtype=int
        )

    solution = part_2(hiking_map)

    print("Advent of Code 2024 (day 10 - Python)")
    print(f"Solution for part 2: {solution}")
