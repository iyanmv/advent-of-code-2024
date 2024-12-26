from pathlib import Path
from itertools import product

import numpy as np

module_path = Path(__file__).resolve().parent


def parse_input(text):
    keys = []
    locks = []
    for s in text.split("\n\n"):
        arr = np.array([[l for l in line] for line in s.splitlines()], dtype="<U1")
        first_row = arr[0, :]
        last_row = arr[-1, :]
        if np.all(first_row == "#") and np.all(last_row == "."):
            locks.append(arr)
        elif np.all(first_row == ".") and np.all(last_row == "#"):
            keys.append(arr)
        else:
            raise ValueError("Unknown input")
    return keys, locks


def get_heights(list_arr):
    out = []
    for arr in list_arr:
        if np.all(arr[0, :] == "."):
            arr = np.flip(arr, axis=0)
        out.append(np.sum(arr == "#", axis=0) - 1)
    return out


def part_1(keys, locks):
    rows, cols = keys[0].shape
    target = rows - 2
    keys = get_heights(keys)
    locks = get_heights(locks)
    solution = 0
    for key, lock in product(keys, locks):
        if np.all(key + lock <= target):
            solution += 1
    return solution


if __name__ == "__main__":
    with open(module_path / "input", "r") as file:
        keys, locks = parse_input(file.read())

    solution = part_1(keys, locks)

    print("Advent of Code 2024 (day 24 - Python)")
    print(f"Solution for part 1: {solution}")
