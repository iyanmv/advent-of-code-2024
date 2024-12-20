from pathlib import Path

import numpy as np

module_path = Path(__file__).resolve().parent


def parse_map(text):
    return np.array([[l for l in line] for line in text.splitlines()], dtype="<U1")


def generate_distances_array(mapa):
    curr = tuple(int(n.item()) for n in np.nonzero(mapa == "S"))
    end_pos = tuple(int(n.item()) for n in np.nonzero(mapa == "E"))

    dist_arr = np.full(mapa.shape, -1, dtype=int)
    dist_arr[curr] = 0

    directions = {"R": (0, 1), "L": (0, -1), "U": (-1, 0), "D": (1, 0)}
    while curr != end_pos:
        x, y = curr
        for _, (dx, dy) in directions.items():
            x_next, y_next = x + dx, y + dy
            if mapa[x_next, y_next] == "#":
                continue
            if dist_arr[x_next, y_next] != -1:
                continue
            dist_arr[x_next, y_next] = dist_arr[x, y] + 1
            curr = (x_next, y_next)
    return dist_arr


def part_1(mapa, time_saved):
    dist_arr = generate_distances_array(mapa)
    max_x, max_y = mapa.shape
    cheat_points = ((-1, 1), (0, 2), (1, 1), (2, 0))
    solution = {}
    for x, y in np.argwhere(mapa != "#"):
        for dx, dy in cheat_points:
            x_next, y_next = x + dx, y + dy
            if x_next < 0 or x_next >= max_x or y_next < 0 or y_next >= max_y:
                continue
            if mapa[x_next, y_next] == "#":
                continue
            diff = int(abs(dist_arr[x, y] - dist_arr[x_next, y_next])) - 2
            if diff >= time_saved:
                if diff not in solution:
                    solution[diff] = 1
                else:
                    solution[diff] += 1
    return solution


if __name__ == "__main__":
    with open(module_path / "input", "r") as file:
        mapa = parse_map(file.read())

    solution = sum(part_1(mapa, 100).values())

    print("Advent of Code 2024 (day 20 - Python)")
    print(f"Solution for part 1: {solution}")
