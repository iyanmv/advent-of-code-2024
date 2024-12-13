from pathlib import Path

import numpy as np
import scipy as sp

module_path = Path(__file__).resolve().parent


def part_2(garden_map):
    x, y = garden_map.shape
    plant_types = np.unique(garden_map.flatten())

    padded_map = np.full((x + 2, y + 2), "-", dtype="<U1")
    padded_map[1:-1, 1:-1] = garden_map

    areas = []
    sides = []

    for plant in plant_types:
        labelled_map, n_clusters = sp.ndimage.label(padded_map == plant)
        for i in range(n_clusters):
            target = i + 1
            areas.append((labelled_map == target).sum())
            side = 0
            points = np.argwhere(labelled_map == target)
            for x, y in points:
                NW = labelled_map[x - 1, y - 1]
                N = labelled_map[x - 1, y]
                NE = labelled_map[x - 1, y + 1]
                E = labelled_map[x, y + 1]
                SE = labelled_map[x + 1, y + 1]
                S = labelled_map[x + 1, y]
                SW = labelled_map[x + 1, y - 1]
                W = labelled_map[x, y - 1]
                # Left side
                if W != target:
                    if not (N == target and NW != N):
                        side += 1
                # Right side
                if E != target:
                    if not (N == target and NE != N):
                        side += 1
                # Top side
                if N != target:
                    if not (W == target and NW != W):
                        side += 1
                # Bottom side
                if S != target:
                    if not (W == target and SW != W):
                        side += 1

            sides.append(side)
    return sum([area * side for area, side in zip(areas, sides)])


if __name__ == "__main__":
    with open(module_path / "input", "r") as file:
        garden_map = np.array([[l for l in line] for line in file.read().splitlines()])

    solution = part_2(garden_map)

    print("Advent of Code 2024 (day 12 - Python)")
    print(f"Solution for part 2: {solution}")
