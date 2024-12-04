from pathlib import Path

import numpy as np

module_path = Path(__file__).resolve().parent


def check_xmas(array, row, col):
    possible_positions = [
        # Horizontal right
        [(row, row, row, row), (col, col + 1, col + 2, col + 3)],
        # Horizontal left
        [(row, row, row, row), (col, col - 1, col - 2, col - 3)],
        # Vertical down
        [(row, row + 1, row + 2, row + 3), (col, col, col, col)],
        # Vertical up
        [(row, row - 1, row - 2, row - 3), (col, col, col, col)],
        # Diagonal up right
        [(row, row - 1, row - 2, row - 3), (col, col + 1, col + 2, col + 3)],
        # Diagonal up left
        [(row, row - 1, row - 2, row - 3, row - 4), (col, col - 1, col - 2, col - 3)],
        # Diagonal down right
        [(row, row + 1, row + 2, row + 3), (col, col + 1, col + 2, col + 3)],
        # Diagonal down left
        [(row, row + 1, row + 2, row + 3), (col, col - 1, col - 2, col - 3)],
    ]

    counter = 0
    for x, y in possible_positions:
        text = "".join([array[i, j] for i, j in zip(x, y)])
        if text == "XMAS":
            counter += 1
    return counter


def part_1(text_list):
    text = np.array(text_list)
    padded_arr = np.zeros([_ + 8 for _ in text.shape], dtype="<U1")
    padded_arr[4:-4, 4:-4] = text

    rows, cols = padded_arr.shape
    counter = 0
    for i in range(rows):
        for j in range(cols):
            if padded_arr[i, j] == "X":
                counter += check_xmas(padded_arr, i, j)
    return counter


if __name__ == "__main__":
    text = []
    with open(module_path / "input", "r") as file:
        for line in file:
            text.append([l for l in line.strip()])
    solution = part_1(text)

    print("Advent of Code 2024 (day 4 - Python)")
    print(f"Solution for part 1: {solution}")
