from pathlib import Path

import numpy as np

module_path = Path(__file__).resolve().parent


def part_1(arr):
    arr.sort(axis=0)
    return np.abs(arr[:, 0] - arr[:, 1]).sum()


if __name__ == "__main__":
    input_arr = np.loadtxt(module_path / "input", dtype=int)
    solution = part_1(input_arr)
    print("Advent of Code 2024 (day 1 - Python)")
    print(f"Solution for part 1: {solution}")
