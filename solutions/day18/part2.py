from pathlib import Path

import numpy as np
import networkx as nx

from part1 import generate_graph

module_path = Path(__file__).resolve().parent


def parse_bytes(text):
    return np.loadtxt(text.splitlines(), delimiter=",", dtype=int)


def part_2(corrupted_bytes, size):
    memory = np.full([i + 2 for i in size], "#", dtype="<U1")
    memory[1:-1, 1:-1] = np.full(size, ".", dtype="<U1")

    start_pos = (1, 1)
    end_pos = tuple(i - 2 for i in memory.shape)

    for n, (x, y) in enumerate(corrupted_bytes):
        memory[x + 1, y + 1] = "#"
        if n < 1024:
            continue
        graph = generate_graph(memory)
        try:
            nx.shortest_path(graph, start_pos, end_pos)
        except nx.exception.NetworkXNoPath:
            return f"{x},{y}"


if __name__ == "__main__":
    with open(module_path / "input", "r") as file:
        corrupted_bytes = parse_bytes(file.read())

    solution = part_2(corrupted_bytes, (71, 71))

    print("Advent of Code 2024 (day 18 - Python)")
    print(f"Solution for part 2: {solution}")
