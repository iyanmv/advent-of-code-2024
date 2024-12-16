from pathlib import Path

import numpy as np
import networkx

from part1 import part_1, generate_graph

module_path = Path(__file__).resolve().parent


def parse_maze(text):
    return np.array([[l for l in line] for line in text.splitlines()], dtype="<U1")


def part_2(maze):
    np.set_printoptions(threshold=np.inf)
    np.set_printoptions(linewidth=np.inf)

    graph = generate_graph(maze)

    start_pos = tuple([int(_) for _ in np.argwhere(maze == "S").flatten()])
    end_pos = tuple([int(_) for _ in np.argwhere(maze == "E").flatten()])

    start_node = (*start_pos, "E")
    end_nodes = [(*end_pos, direction) for direction in ["E", "W", "N", "S"]]

    target_cost = part_1(maze)

    tiles = set()
    for end_node in end_nodes:
        try:
            paths = networkx.all_shortest_paths(
                graph, source=start_node, target=end_node, weight="weight"
            )
            for path in paths:
                if not networkx.path_weight(graph, path, weight="weight") > target_cost:
                    for x, y, _ in path:
                        tiles.add((x, y))
        except nx.NetworkXNoPath:
            continue

    return len(tiles)


if __name__ == "__main__":
    with open(module_path / "input", "r") as file:
        maze_map = parse_maze(file.read())

    solution = part_2(maze_map)

    print("Advent of Code 2024 (day 16 - Python)")
    print(f"Solution for part 2: {solution}")
