from pathlib import Path

import numpy as np

module_path = Path(__file__).resolve().parent


def check_xmas(array, row, col):
    view_down = array[row : row + 3, col : col + 3].copy()
    view_up = array[row : row - 3 : -1, col : col - 3 : -1].copy()
    view_up[(0, 2), 1] = ""
    view_up[1, (0, 2)] = ""
    view_down[(0, 2), 1] = ""
    view_down[1, (0, 2)] = ""

    valid_arrays = [
        np.array([["M", "", "S"], ["", "A", ""], ["M", "", "S"]]),
        np.array([["M", "", "M"], ["", "A", ""], ["S", "", "S"]]),
        np.array([["S", "", "S"], ["", "A", ""], ["M", "-", "M"]]),
        np.array([["S", "", "M"], ["", "A", ""], ["S", "", "M"]]),
    ]

    counter = 0
    for arr in valid_arrays:
        if np.array_equal(view_up, arr):
            counter += 1
        if np.array_equal(view_down, arr):
            counter += 1
    return counter


def part_2(text_list):
    text = np.array(text_list)
    padded_arr = np.zeros([_ + 6 for _ in text.shape], dtype="<U1")
    padded_arr[3:-3, 3:-3] = text

    rows, cols = padded_arr.shape
    counter = 0
    for i in range(rows):
        for j in range(cols):
            if padded_arr[i, j] == "M":
                counter += check_xmas(padded_arr, i, j)
    return counter


if __name__ == "__main__":
    text = []
    with open(module_path / "input", "r") as file:
        for line in file:
            text.append([l for l in line.strip()])
    solution = part_2(text)

    print("Advent of Code 2024 (day 4 - Python)")
    print(f"Solution for part 2: {solution}")
