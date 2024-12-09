from pathlib import Path
from itertools import combinations

from gmpy2 import gcd
import numpy as np

from part1 import localize_antennas

module_path = Path(__file__).resolve().parent


def compute_antinodes(antenna_1, antenna_2, max_x, max_y):
    x1, y1 = antenna_1
    x2, y2 = antenna_2
    div = int(gcd(x1, x2, y1, y2))
    unit_x, unit_y = ((x2 - x1) // div, (y2 - y1) // div)
    antinodes = set()

    count = 0
    while True:
        next_x, next_y = x2 + count * unit_x, y2 + count * unit_y
        if next_x < 0 or next_x >= max_x or next_y < 0 or next_y >= max_y:
            break

        antinodes.add((next_x, next_y))
        count += 1

    count = 0
    while True:
        next_x, next_y = x1 - count * unit_x, y1 - count * unit_y
        if next_x < 0 or next_x >= max_x or next_y < 0 or next_y >= max_y:
            break

        antinodes.add((next_x, next_y))
        count += 1

    return antinodes


def part_2(input_map):
    max_x, max_y = input_map.shape

    antennas = localize_antennas(input_map)
    antinodes = set()

    for i, freq in enumerate(antennas):
        new_nodes = set()
        for pos_1, pos_2 in combinations(antennas[freq], 2):
            antinodes.update(compute_antinodes(pos_1, pos_2, max_x, max_y))

    return len(antinodes)


if __name__ == "__main__":
    with open(module_path / "input", "r") as file:
        data = file.read()
    map_antennas = np.array([[letter for letter in line] for line in data.splitlines()])

    solution = part_2(map_antennas)

    print("Advent of Code 2024 (day 8 - Python)")
    print(f"Solution for part 2: {solution}")
