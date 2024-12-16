from pathlib import Path

import numpy as np
import networkx

module_path = Path(__file__).resolve().parent


def parse_maze(text):
    return np.array([[l for l in line] for line in text.splitlines()], dtype="<U1")


def generate_graph(maze_arr):
    directions = {"E": (0, 1), "W": (0, -1), "N": (-1, 0), "S": (1, 0)}
    clock_rotation = {"E": "S", "S": "W", "W": "N", "N": "E"}
    anticlock_rotation = {"E": "N", "N": "W", "W": "S", "S": "E"}

    graph = networkx.DiGraph()

    for x, y in np.argwhere(maze_arr != "#"):
        x, y = map(int, (x, y))
        for direction, (dx, dy) in directions.items():
            current = (x, y, direction)
            nx, ny = x + dx, y + dy
            if maze_arr[nx, ny] != "#":
                graph.add_edge(current, (nx, ny, direction), weight=1)
            graph.add_edge(current, (x, y, clock_rotation[direction]), weight=1000)
            graph.add_edge(current, (x, y, anticlock_rotation[direction]), weight=1000)

    return graph


def part_1(maze):
    graph = generate_graph(maze)

    start_pos = tuple([int(_) for _ in np.argwhere(maze == "S").flatten()])
    end_pos = tuple([int(_) for _ in np.argwhere(maze == "E").flatten()])

    start_node = (*start_pos, "E")
    end_nodes = [(*end_pos, direction) for direction in ["E", "W", "N", "S"]]

    shortest_cost = float("inf")

    for end_node in end_nodes:
        try:
            cost = networkx.shortest_path_length(
                graph, source=start_node, target=end_node, weight="weight"
            )
            if cost < shortest_cost:
                shortest_cost = cost
        except nx.NetworkXNoPath:
            continue

    return shortest_cost


if __name__ == "__main__":
    with open(module_path / "input", "r") as file:
        maze_map = parse_maze(file.read())

    solution = part_1(maze_map)

    print("Advent of Code 2024 (day 16 - Python)")
    print(f"Solution for part 1: {solution}")
