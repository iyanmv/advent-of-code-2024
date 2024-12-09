from pathlib import Path
from itertools import combinations

import numpy as np

module_path = Path(__file__).resolve().parent


def localize_antennas(input_map):
    frequencies = set(input_map.flatten())
    frequencies.remove(".")
    antennas = {}
    for freq in frequencies:
        antennas[str(freq)] = np.argwhere(input_map == freq).tolist()
    return antennas


def compute_antinodes(antenna_1, antenna_2):
    x1, y1 = antenna_1
    x2, y2 = antenna_2
    antinode_1 = (2 * x1 - x2, 2 * y1 - y2)
    antinode_2 = (2 * x2 - x1, 2 * y2 - y1)
    return antinode_1, antinode_2


def part_1(input_map):
    max_x, max_y = input_map.shape

    antennas = localize_antennas(input_map)
    antinodes = []

    for freq in antennas:
        for pos_1, pos_2 in combinations(antennas[freq], 2):
            points = compute_antinodes(pos_1, pos_2)

            for x, y in points:
                if 0 <= x < max_x and 0 <= y < max_y and [x, y] not in antinodes:
                    antinodes.append([x, y])

    return len(antinodes)


if __name__ == "__main__":
    with open(module_path / "input", "r") as file:
        data = file.read()
    map_antennas = np.array([[letter for letter in line] for line in data.splitlines()])

    solution = part_1(map_antennas)

    print("Advent of Code 2024 (day 8 - Python)")
    print(f"Solution for part 1: {solution}")
