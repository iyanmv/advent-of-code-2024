from pathlib import Path

import numpy as np
import networkx as nx

module_path = Path(__file__).resolve().parent


def parse_memory(text, n_bytes, size):
    corruption_positions = np.loadtxt(text.splitlines(), delimiter=",", dtype=int)
    temp = np.full(size, ".", dtype="<U1")
    temp[corruption_positions[:n_bytes, 1], corruption_positions[:n_bytes, 0]] = "#"
    memory = np.full([i + 2 for i in size], "#", dtype="<U1")
    memory[1:-1, 1:-1] = temp
    return memory


def generate_graph(memory_arr):
    directions = {"R": (0, 1), "L": (0, -1), "U": (-1, 0), "D": (1, 0)}

    graph = nx.DiGraph()

    for x, y in np.argwhere(memory_arr != "#"):
        x, y = map(int, (x, y))
        for direction, (dx, dy) in directions.items():
            current = (x, y)
            x_next, y_next = x + dx, y + dy
            if memory_arr[x_next, y_next] != "#":
                graph.add_edge(current, (x_next, y_next))

    return graph


def part_1(memory_arr):
    graph = generate_graph(memory_arr)
    start_pos = (1, 1)
    end_pos = tuple(i - 2 for i in memory_arr.shape)
    shortest_path = nx.shortest_path(graph, start_pos, end_pos)
    return len(shortest_path) - 1


if __name__ == "__main__":
    with open(module_path / "input", "r") as file:
        memory_arr = parse_memory(file.read(), 1024, (71, 71))

    solution = part_1(memory_arr)

    print("Advent of Code 2024 (day 18 - Python)")
    print(f"Solution for part 1: {solution}")
