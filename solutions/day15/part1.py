from pathlib import Path

import numpy as np

module_path = Path(__file__).resolve().parent


def parse_map(text):
    initial_map, instructions = text.split("\n\n")
    initial_map = np.array(
        [[l for l in line] for line in initial_map.splitlines()], dtype="<U1"
    )
    instructions = instructions.replace("\n", "")
    return initial_map, instructions


def get_next_pos(i, j, move):
    moves = {"<": (0, -1), "^": (-1, 0), ">": (0, 1), "v": (1, 0)}
    i_next, j_next = tuple([sum(x) for x in zip((i, j), moves[move])])
    return i_next, j_next


def make_move(move, final_map):
    i, j = np.nonzero(final_map == "@")
    i_next, j_next = get_next_pos(i, j, move)

    if final_map[i_next, j_next] == "#":
        return
    elif final_map[i_next, j_next] == ".":
        final_map[i_next, j_next] = "@"
        final_map[i, j] = "."
    elif final_map[i_next, j_next] == "O":
        count = 1
        while True:
            i_next_next, j_next_next = get_next_pos(i_next, j_next, move)
            if final_map[i_next_next, j_next_next] == "#":
                return
            elif final_map[i_next_next, j_next_next] == "O":
                i_next, j_next = i_next_next, j_next_next
                count += 1
                continue
            elif final_map[i_next_next, j_next_next] == ".":
                break

        i_next, j_next = get_next_pos(i, j, move)
        final_map[i, j] = "."
        final_map[i_next, j_next] = "@"
        for _ in range(count):
            i_next_next, j_next_next = get_next_pos(i_next, j_next, move)
            final_map[i_next_next, j_next_next] = "O"
            i_next, j_next = i_next_next, j_next_next


def simulate(initial_map, instructions):
    final_map = initial_map.copy()
    for move in instructions:
        make_move(move, final_map)
    return final_map


def part_1(initial_map, instructions):
    final_map = simulate(initial_map, instructions)
    return np.sum(np.argwhere(final_map == "O") @ np.array([100, 1]))


if __name__ == "__main__":
    with open(module_path / "input", "r") as file:
        initial_map, instructions = parse_map(file.read())

    solution = part_1(initial_map, instructions)

    print("Advent of Code 2024 (day 15 - Python)")
    print(f"Solution for part 1: {solution}")
