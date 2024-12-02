from pathlib import Path

import numpy as np

module_path = Path(__file__).resolve().parent


def check_line(list_numbers):
    errors = []
    prev_increasing = None

    for i in range(len(list_numbers) - 1):
        n_0 = list_numbers[i]
        n_1 = list_numbers[i + 1]
        increasing = n_1 >= n_0
        if prev_increasing is not None:
            if increasing != prev_increasing:
                errors.append(i)
        prev_increasing = increasing
        diff = abs(n_1 - n_0)
        if diff < 1 or diff > 3:
            errors.append(i)

    return errors


def is_report_safe(line):
    numbers = [int(n) for n in line.strip().split(" ")]
    errors = check_line(numbers)

    if len(errors) == 0:
        return True

    for err in errors:
        for test_err in [err - 1, err, err + 1]:
            alt_numbers = numbers.copy()
            del alt_numbers[test_err]
            alt_errors = check_line(alt_numbers)
            if len(alt_errors) == 0:
                return True

    return False


def part_2(file_generator):
    sol = 0
    for line in file_generator:
        if is_report_safe(line):
            sol += 1
    return sol


if __name__ == "__main__":
    with open(module_path / "input", "r") as file:
        solution = part_2(file)

    print("Advent of Code 2024 (day 2 - Python)")
    print(f"Solution for part 2: {solution}")
