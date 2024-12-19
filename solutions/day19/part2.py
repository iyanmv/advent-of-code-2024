from pathlib import Path

import numpy as np

from part1 import parse_towels, count_patterns

module_path = Path(__file__).resolve().parent


def part_2(towels, patterns):
    solution = 0

    for pattern in patterns:
        solution += count_patterns(pattern, towels)

    return solution


if __name__ == "__main__":
    with open(module_path / "input", "r") as file:
        towels, patterns = parse_towels(file.read())

    solution = part_2(towels, patterns)

    print("Advent of Code 2024 (day 19 - Python)")
    print(f"Solution for part 2: {solution}")
