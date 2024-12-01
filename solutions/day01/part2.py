from pathlib import Path

import numpy as np

module_path = Path(__file__).resolve().parent


def part_2(arr):
    solution = 0
    for num in arr[:, 0]:
        solution += num * (arr[:, 1] == num).sum()
    return solution


if __name__ == "__main__":
    input_arr = np.loadtxt(module_path / "input", dtype=int)
    solution = part_2(input_arr)
    print("Advent of Code 2024 (day 1)")
    print(f"Solution for part 2: {solution}")
