from pathlib import Path

import numpy as np

module_path = Path(__file__).resolve().parent


def is_valid(update, rules):
    update = np.array(update, dtype=int)
    for number in update:
        relevant_rules = rules[np.any(rules == number, axis=1)]
        for x, y in relevant_rules:
            arg_x = np.argwhere(update == x)
            arg_y = np.argwhere(update == y)
            if arg_x.size == 0 or arg_y.size == 0:
                continue
            if arg_x > arg_y:
                return False
    return True


def part_1(rules, updates):
    solution = 0
    for update in updates:
        if is_valid(update, rules):
            solution += update[len(update) // 2]
    return solution


if __name__ == "__main__":
    rules = np.loadtxt(module_path / "input", delimiter="|", max_rows=1176, dtype=int)
    updates = []
    with open("input", "r") as file:
        skip = True
        for line in file:
            if line == "\n":
                skip = False
                continue
            if skip:
                continue
            updates.append([int(num) for num in line.strip().split(",")])

    solution = part_1(rules, updates)

    print("Advent of Code 2024 (day 5 - Python)")
    print(f"Solution for part 1: {solution}")
