from pathlib import Path

import numpy as np

module_path = Path(__file__).resolve().parent


def parse_towels(text):
    towels, patterns = text.split("\n\n")
    towels = set([_.strip() for _ in towels.split(",")])
    patterns = patterns.splitlines()
    return towels, patterns


def count_patterns(target, towels, known={}):
    if target == "":
        return 1

    if target in known:
        return known[target]

    total = 0
    for towel in towels:
        if target.startswith(towel):
            total += count_patterns(target[len(towel):], towels, known)

    known[target] = total
    return total


def part_1(towels, patterns):
    solution = 0

    for pattern in patterns:
        if count_patterns(pattern, towels) > 0:
            solution += 1

    return solution


if __name__ == "__main__":
    with open(module_path / "input", "r") as file:
        towels, patterns = parse_towels(file.read())

    solution = part_1(towels, patterns)

    print("Advent of Code 2024 (day 19 - Python)")
    print(f"Solution for part 1: {solution}")
