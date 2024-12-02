from pathlib import Path

import numpy as np

module_path = Path(__file__).resolve().parent


def is_report_safe(line):
    numbers = [int(n) for n in line.strip().split(" ")]
    prev_increasing = None
    for i in range(len(numbers) - 1):
        n_0 = numbers[i]
        n_1 = numbers[i + 1]
        increasing = n_1 >= n_0
        if prev_increasing is not None:
            if increasing != prev_increasing:
                return False
        prev_increasing = increasing
        diff = abs(n_1 - n_0)
        if diff < 1 or diff > 3:
            return False
    return True


def part_1(file_generator):
    sol = 0
    for line in file_generator:
        if is_report_safe(line):
            sol += 1
    return sol


if __name__ == "__main__":
    with open(module_path / "input", "r") as file:
        solution = part_1(file)

    print("Advent of Code 2024 (day 2 - Python)")
    print(f"Solution for part 1: {solution}")
    