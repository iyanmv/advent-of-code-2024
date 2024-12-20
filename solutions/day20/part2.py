from pathlib import Path

import numpy as np

from part1 import parse_map, generate_distances_array

module_path = Path(__file__).resolve().parent


def part_2(mapa, time_saved, cheat_time):
    np.set_printoptions(threshold=np.inf)
    np.set_printoptions(linewidth=np.inf)
    dist_arr = generate_distances_array(mapa)
    max_x, max_y = mapa.shape
    solution = {}
    for x, y in np.argwhere(mapa != "#"):
        for radius in range(2, cheat_time + 1):
            for dx in range(radius + 1):
                dy = radius - dx
                cheat_points = {(x + dx, y + dy), (x + dx, y - dy), (x - dx, y + dy), (x - dx, y - dy)}
                for x_next, y_next in cheat_points:
                    if x_next < 0 or x_next >= max_x or y_next < 0 or y_next >= max_y:
                        continue
                    if mapa[x_next, y_next] == "#":
                        continue
                    diff = int(dist_arr[x, y] - dist_arr[x_next, y_next]) - radius
                    if diff >= time_saved:
                        if diff not in solution:
                            solution[diff] = 1
                        else:
                            solution[diff] += 1
    return solution


if __name__ == "__main__":
    with open(module_path / "input", "r") as file:
        mapa = parse_map(file.read())

    solution = sum(part_2(mapa, 100, 20).values())

    print("Advent of Code 2024 (day 20 - Python)")
    print(f"Solution for part 2: {solution}")
