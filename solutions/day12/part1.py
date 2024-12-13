from pathlib import Path

import numpy as np
import scipy as sp

module_path = Path(__file__).resolve().parent


def part_1(garden_map):
    x, y = garden_map.shape
    mask = np.array([[False, True, False], [True, False, True], [False, True, False]])
    plant_types = np.unique(garden_map.flatten())

    padded_map = np.full((x + 2, y + 2), "-", dtype="<U1")
    padded_map[1:-1, 1:-1] = garden_map

    areas = []
    perimeters = []

    for plant in plant_types:
        labelled_map, n_clusters = sp.ndimage.label(padded_map == plant)
        for i in range(n_clusters):
            areas.append((labelled_map == i + 1).sum())
            perimeter = 0
            for x, y in np.argwhere(labelled_map == i + 1):
                perimeter += np.logical_and(
                    labelled_map[x - 1 : x + 2, y - 1 : y + 2] != i + 1, mask
                ).sum()
            perimeters.append(perimeter)

    return sum([area * perimeter for area, perimeter in zip(areas, perimeters)])


if __name__ == "__main__":
    with open(module_path / "input", "r") as file:
        garden_map = np.array([[l for l in line] for line in file.read().splitlines()])

    solution = part_1(garden_map)

    print("Advent of Code 2024 (day 12 - Python)")
    print(f"Solution for part 1: {solution}")
