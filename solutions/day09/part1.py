from pathlib import Path

import numpy as np

module_path = Path(__file__).resolve().parent


def obtain_layout(disk_map):
    total_bytes = sum([int(n) for n in disk_map])
    layout = np.zeros(total_bytes, dtype=int)

    file = True
    file_id = 0
    index_layout = 0

    for digit in disk_map:
        digit = int(digit)
        if file:
            layout[index_layout : index_layout + digit] = file_id
            file_id += 1
        else:
            layout[index_layout : index_layout + digit] = -1

        index_layout += digit
        file = not file

    return layout


def compact_disk(layout):
    emtpy_parts = (layout == -1).sum()
    files = layout[layout != -1]
    layout[layout == -1] = files[-1 : -(emtpy_parts + 1) : -1]
    layout[-emtpy_parts:] = -1


def checksum(layout):
    files = layout[layout != -1]
    return (files * np.arange(files.size)).sum()


def part_1(disk_map):
    layout = obtain_layout(disk_map)
    compact_disk(layout)
    return checksum(layout)


if __name__ == "__main__":
    with open(module_path / "input", "r") as file:
        disk_map = file.read().strip()

    solution = part_1(disk_map)

    print("Advent of Code 2024 (day 9 - Python)")
    print(f"Solution for part 1: {solution}")
