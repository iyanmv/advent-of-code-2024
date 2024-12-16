from pathlib import Path

import numpy as np

from part1 import parse_map, get_next_pos

module_path = Path(__file__).resolve().parent


def convert_map(initial_map):
    rows, cols = initial_map.shape
    new_map = np.zeros((rows, 2 * cols), dtype="<U1")
    for i in range(rows):
        for j in range(cols):
            val = initial_map[i, j]
            if val == "#":
                new_map[i, 2 * j : 2 * (j + 1)] = np.array(["#", "#"])
            elif val == "O":
                new_map[i, 2 * j : 2 * (j + 1)] = np.array(["[", "]"])
            elif val == ".":
                new_map[i, 2 * j : 2 * (j + 1)] = np.array([".", "."])
            elif val == "@":
                new_map[i, 2 * j : 2 * (j + 1)] = np.array(["@", "."])
    return new_map


def generate_mask(i, j, move, final_map):
    points = {(i, j)}

    if move == "^":
        i -= 1
    else:
        i += 1

    if final_map[i, j] == "#":
        return None

    if final_map[i, j] == ".":
        return points

    if final_map[i, j] == "[":
        new_points = generate_mask(i, j, move, final_map)
        if new_points is None:
            return None
        points.update(new_points)
        new_points = generate_mask(i, j + 1, move, final_map)
        if new_points is None:
            return None
        points.update(new_points)

    elif final_map[i, j] == "]":
        new_points = generate_mask(i, j, move, final_map)
        if new_points is None:
            return None
        points.update(new_points)
        new_points = generate_mask(i, j - 1, move, final_map)
        if new_points is None:
            return None
        points.update(new_points)

    return points


def make_move(move, final_map):
    i, j = np.argwhere(final_map == "@").flatten()

    if move == "<":
        arr = np.argwhere(final_map[i, :j] == ".")
        if arr.size == 0:
            return
        first_empty = arr.max()
        first_wall = np.argwhere(final_map[i, :j] == "#").max()
        if first_empty > first_wall:
            final_map[i, first_empty:j] = final_map[i, first_empty + 1 : j + 1]
            final_map[i, j] = "."

    elif move == ">":
        arr = np.argwhere(final_map[i, j + 1 :] == ".")
        if arr.size == 0:
            return
        first_empty = arr.min() + j
        first_wall = np.argwhere(final_map[i, j + 1 :] == "#").min() + j
        if first_empty < first_wall:
            final_map[i, j + 1 : first_empty + 2] = final_map[i, j : first_empty + 1]
            final_map[i, j] = "."

    elif move == "v":
        if final_map[i + 1, j] == "#":
            return

        elif final_map[i + 1, j] == ".":
            final_map[i + 1, j] = "@"
            final_map[i, j] = "."
            return

        else:
            move_mask = generate_mask(i, j, move, final_map)
            if move_mask is None:
                return
            for x, y in sorted(move_mask, reverse=True):
                final_map[x + 1, y] = final_map[x, y]
                if (x - 1, y) not in move_mask:
                    final_map[x, y] = "."

    elif move == "^":
        if final_map[i - 1, j] == "#":
            return

        elif final_map[i - 1, j] == ".":
            final_map[i - 1, j] = "@"
            final_map[i, j] = "."

        else:
            move_mask = generate_mask(i, j, move, final_map)
            if move_mask is None:
                return
            for x, y in sorted(move_mask):
                final_map[x - 1, y] = final_map[x, y]
                if (x + 1, y) not in move_mask:
                    final_map[x, y] = "."


def simulate(initial_map, instructions):
    final_map = initial_map.copy()
    for i, move in enumerate(instructions):
        make_move(move, final_map)
    return final_map


def part_2(initial_map, instructions):
    initial_map = convert_map(initial_map)
    final_map = simulate(initial_map, instructions)
    return np.sum(np.argwhere(final_map == "[") @ np.array([100, 1]))


if __name__ == "__main__":
    with open(module_path / "input", "r") as file:
        initial_map, instructions = parse_map(file.read())

    solution = part_2(initial_map, instructions)

    print("Advent of Code 2024 (day 15 - Python)")
    print(f"Solution for part 2: {solution}")
