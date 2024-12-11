from pathlib import Path

import numpy as np

module_path = Path(__file__).resolve().parent


def compute_score(pos_trailhead, hiking_map):
    curr_pos = [pos_trailhead.tolist()]
    filter = np.array([[False, True, False], [True, True, True], [False, True, False]])
    for step in range(1, 10):
        new_curr_pos = np.array([], dtype=int).reshape(0, 2)
        for x, y in curr_pos:
            new_curr_pos = np.concatenate(
                (
                    new_curr_pos,
                    np.argwhere(
                        # The filer array is used to avoid considering diagonal moves
                        np.logical_and(
                            hiking_map[x - 1 : x + 2, y - 1 : y + 2] == step, filter
                        )
                    )
                    + np.array([x - 1, y - 1]),
                ),
                axis=0,
            )
        if len(new_curr_pos) == 0:
            return 0
        curr_pos = np.unique(new_curr_pos, axis=0)
    return len(curr_pos)


def part_1(hiking_map):
    rows, cols = hiking_map.shape
    padded_map = -1 * np.ones((rows + 2, cols + 2), dtype=int)
    padded_map[1:-1, 1:-1] = hiking_map
    trailheads = np.argwhere(padded_map == 0)

    scores = []
    for trailhead in trailheads:
        scores.append(compute_score(trailhead, padded_map))

    return sum(scores)


if __name__ == "__main__":
    with open(module_path / "input", "r") as file:
        hiking_map = np.array(
            [[n for n in line] for line in file.read().splitlines()], dtype=int
        )

    solution = part_1(hiking_map)

    print("Advent of Code 2024 (day 10 - Python)")
    print(f"Solution for part 1: {solution}")
