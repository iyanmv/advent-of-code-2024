from pathlib import Path

import networkx as nx


module_path = Path(__file__).resolve().parent


def parse_computers(text):
    computers = []
    for line in text.splitlines():
        a, b = line.strip().split("-")
        computers.append((a, b))
    return computers


def generate_graph(computers):
    graph = nx.Graph()
    for a, b in computers:
        graph.add_edge(a, b)
    return graph


def part_1(computers):
    graph = generate_graph(computers)
    connected_computers = [s for s in nx.enumerate_all_cliques(graph) if len(s) == 3]
    filtered_connected_computers = []
    for s in connected_computers:
        for x in s:
            if x.startswith("t"):
                filtered_connected_computers.append(s)
                break

    return len(filtered_connected_computers)


if __name__ == "__main__":
    with open(module_path / "input", "r") as file:
        computers = parse_computers(file.read())

    solution = part_1(computers)

    print("Advent of Code 2024 (day 23 - Python)")
    print(f"Solution for part 1: {solution}")
