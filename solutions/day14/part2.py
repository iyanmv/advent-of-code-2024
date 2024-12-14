from pathlib import Path

import numpy as np

from part1 import part_1, parse_robots

module_path = Path(__file__).resolve().parent


def part_2(robots, size):
    round = 0

    safety_values = []

    while round < 10_000:
        safety_values.append(part_1(robots, size, round))
        round += 1

    return np.argmin(np.array(safety_values))


if __name__ == "__main__":
    with open(module_path / "input", "r") as file:
        initial_robots = parse_robots(file.read())

    solution = part_2(initial_robots, (103, 101))

    print("Advent of Code 2024 (day 14 - Python)")
    print(f"Solution for part 2: {solution}")
