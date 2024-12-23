from pathlib import Path

import networkx as nx

from part1 import parse_computers, generate_graph


module_path = Path(__file__).resolve().parent


def part_2(computers):
    graph = generate_graph(computers)
    subgraphs = list(nx.find_cliques(graph))
    largest_network = max(subgraphs, key=len)
    password = ",".join(sorted(largest_network))
    return password


if __name__ == "__main__":
    with open(module_path / "input", "r") as file:
        computers = parse_computers(file.read())

    solution = part_2(computers)

    print("Advent of Code 2024 (day 23 - Python)")
    print(f"Solution for part 2: {solution}")
