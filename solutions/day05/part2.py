from pathlib import Path

from graph import Graph
import numpy as np

module_path = Path(__file__).resolve().parent

from part1 import is_valid


def generate_new_update(update, rules):
    graph = Graph()
    for x, y in rules:
        if x in update or y in update:
            graph.add_edge(int(x), int(y))
    return [num for num in graph.topological_sort() if num in update]


def part_2(rules, updates):
    solution = 0

    for update in updates:
        if not is_valid(update, rules):
            new_update = generate_new_update(update, rules)
            solution += new_update[len(new_update) // 2]

    return solution


if __name__ == "__main__":
    rules = np.loadtxt("input", delimiter="|", max_rows=1176, dtype=int)
    updates = []
    with open("input", "r") as file:
        skip = True
        for line in file:
            if line == "\n":
                skip = False
                continue
            if skip:
                continue
            updates.append([int(num) for num in line.strip().split(",")])

    solution = part_2(rules, updates)

    print("Advent of Code 2024 (day 5 - Python)")
    print(f"Solution for part 2: {solution}")
