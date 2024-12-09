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
    is_emtpy = layout == -1

    empty_starts = np.where(
        np.diff(np.concatenate(([0], is_emtpy.astype(int), [0]))) == 1
    )[0]
    empty_ends = np.where(
        np.diff(np.concatenate(([0], is_emtpy.astype(int), [0]))) == -1
    )[0]
    empty_lengths = empty_ends - empty_starts

    file_id = layout[-1]
    while file_id > 0:
        size_file = np.sum(layout == file_id)
        start_file = np.where(layout == file_id)[0][0]
        for i, length in enumerate(empty_lengths):
            if length >= size_file and start_file > empty_starts[i]:
                layout[layout == file_id] = -1
                layout[empty_starts[i] : empty_starts[i] + size_file] = file_id
                empty_starts[i] = empty_starts[i] + size_file
                empty_lengths[i] -= size_file
                break
        file_id -= 1


def checksum(layout):
    return (np.where(layout != -1, layout, 0) * np.arange(layout.size)).sum()


def part_2(disk_map):
    layout = obtain_layout(disk_map)
    compact_disk(layout)
    return checksum(layout)


if __name__ == "__main__":
    with open(module_path / "input", "r") as file:
        disk_map = file.read().strip()

    solution = part_2(disk_map)

    print("Advent of Code 2024 (day 9 - Python)")
    print(f"Solution for part 2: {solution}")
