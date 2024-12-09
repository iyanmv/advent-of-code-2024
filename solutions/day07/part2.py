from math import prod
from pathlib import Path

from gmpy2 import digits

module_path = Path(__file__).resolve().parent


def compute_number(numbers, operations, target):
    temp = numbers[0]
    for i in range(len(operations)):
        if operations[i] == "0":
            temp += numbers[i + 1]
        elif operations[i] == "1":
            temp *= numbers[i + 1]
        else:
            temp = int(f"{temp}{numbers[i + 1]}")

        if temp > target:
            return None

    return temp


def part_2(calibrations):
    solution = 0
    for target, numbers in calibrations:
        if sum(numbers) > target > prod(numbers):
            continue

        n_operations = len(numbers) - 1
        n_permutations = 3**n_operations

        for i in range(n_permutations):
            operations = digits(i, 3).rjust(n_operations, "0")
            output = compute_number(numbers, operations, target)

            if output == target:
                solution += target
                break

    return solution


if __name__ == "__main__":
    calibrations = []
    with open(module_path / "input", "r") as file:
        for line in file:
            target, numbers = line.strip().split(":")
            target = int(target)
            numbers = [int(n) for n in numbers.split()]
            calibrations.append((target, numbers))

    solution = part_2(calibrations)

    print("Advent of Code 2024 (day 7 - Python)")
    print(f"Solution for part 2: {solution}")
