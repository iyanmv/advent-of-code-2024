from pathlib import Path
from functools import cmp_to_key

import numpy as np

module_path = Path(__file__).resolve().parent

from part1 import is_valid


def compare_numbers(x, y):
    global rules_dict
    if (x, y) not in rules_dict:
        return 0
    elif rules_dict[(x, y)]:
        return -1
    return 1


def part_2(rules, updates):
    global rules_dict
    rules_dict = dict([((int(x), int(y)), True) for x, y in rules])
    solution = 0
    for update in updates:
        if not is_valid(update, rules):
            new_update = sorted(update, key=cmp_to_key(compare_numbers))
            solution += new_update[len(new_update) // 2]
    return solution


if __name__ == "__main__":
    rules = np.loadtxt(module_path / "input", delimiter="|", max_rows=1176, dtype=int)
    updates = []
    with open(module_path / "input", "r") as file:
        skip = True
        for line in file:
            if line == "\n":
                skip = False
                continue
            if skip:
                continue
            updates.append([int(num) for num in line.strip().split(",")])

    solution = part_2(rules, updates)

    print("Advent of Code 2024 (day 5 - Python)")
    print(f"Solution for part 2: {solution}")
