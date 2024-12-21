from pathlib import Path

import networkx as nx
import numpy as np

module_path = Path(__file__).resolve().parent


def generate_graph(arr):
    directions = {"R": (0, 1), "L": (0, -1), "U": (-1, 0), "D": (1, 0)}
    x_max, y_max = arr.shape
    graph = nx.DiGraph()
    for x, y in np.argwhere(arr != "-"):
        for _, (dx, dy) in directions.items():
            x_next, y_next = x + dx, y + dy
            if x_next < 0 or x_next >= x_max or y_next < 0 or y_next >= y_max:
                continue
            if arr[x_next, y_next] == "-":
                continue
            graph.add_edge((x, y), (x_next, y_next))
    return graph


def generate_numeric_pad():
    """
    +---+---+---+
    | 7 | 8 | 9 |
    +---+---+---+
    | 4 | 5 | 6 |
    +---+---+---+
    | 1 | 2 | 3 |
    +---+---+---+
        | 0 | A |
        +---+---+
    """
    # fmt: off
    numeric_pad = np.array([
        ["7", "8", "9"],
        ["4", "5", "6"],
        ["1", "2", "3"],
        ["-", "0", "A"]], dtype="<U1")
    number_to_pos = {
        "7": (0, 0), "8": (0, 1), "9": (0, 2),
        "4": (1, 0), "5": (1, 1), "6": (1, 2),
        "1": (2, 0), "2": (2, 1), "3": (2, 2),
        "0": (3, 1), "A": (3, 2)
    }
    pos_to_number = {
        (0, 0): "7", (0, 1): "8", (0, 2): "9",
        (1, 0): "4", (1, 1): "5", (1, 2): "6",
        (2, 0): "1", (2, 1): "2", (2, 2): "3",
        (3, 1): "0", (3, 2): "A"
    }
    # fmt: on
    graph = generate_graph(numeric_pad)
    return number_to_pos, pos_to_number, graph


def generate_keypad():
    """
        +---+---+
        | ^ | A |
    +---+---+---+
    | < | v | > |
    +---+---+---+
    """
    # fmt: off
    keypad = np.array([
        ["-", "^", "A"],
        ["<", "v", ">"]], dtype="<U1")
    key_to_pos = {
        "^": (0, 1), "A": (0, 2),
        "<": (1, 0), "v": (1, 1), ">": (1, 2)
    }
    pos_to_key = {
        (0, 1): "^", (0, 2): "A",
        (1, 0): "<", (1, 1): "v", (1, 2): ">"
    }
    # fmt: on
    graph = generate_graph(keypad)
    return key_to_pos, pos_to_key, graph


def get_sequences(seq, pad):
    directions = {(0, -1): "<", (0, 1): ">", (-1, 0): "^", (1, 0): "v"}
    sym_to_pos, pos_to_sym, graph = pad
    curr_pos = sym_to_pos["A"]
    sequences = []

    for i in range(len(seq)):
        next_sym = seq[i]
        next_pos = sym_to_pos[next_sym]
        paths = nx.all_shortest_paths(graph, curr_pos, next_pos)
        curr_seqs = []
        for path in paths:
            out = ""
            curr_pos = path[-1]
            for j in range(1, len(path)):
                direction = tuple(np - cp for cp, np in zip(path[j - 1], path[j]))
                key = directions[direction]
                out += key
            out += "A"
            curr_seqs.append(out)

        if len(sequences) == 0:
            for s in curr_seqs:
                sequences.append(s)
        else:
            new_sequences = []
            for j in range(len(sequences)):
                for s in curr_seqs:
                    new_sequences.append(sequences[j] + s)
            sequences = new_sequences

    return sequences


def part_1(pins):
    numpad = generate_numeric_pad()
    keypad = generate_keypad()

    solution = 0

    for pin in pins:
        robot_1_seqs = get_sequences(pin, numpad)
        robot_2_seqs = set()
        for rb1 in robot_1_seqs:
            robot_2_seqs.update(set(get_sequences(rb1, keypad)))
        min_len = min(map(len, robot_2_seqs))
        robot_2_seqs = [s for s in robot_2_seqs if len(s) == min_len]
        manual_seqs = set()
        for rb2 in robot_2_seqs:
            manual_seqs.update(set(get_sequences(rb2, keypad)))
        solution += len(min(manual_seqs, key=len)) * int(pin[:-1])

    return solution


if __name__ == "__main__":
    with open(module_path / "input", "r") as file:
        pins = file.read().splitlines()

    solution = part_1(pins)

    print("Advent of Code 2024 (day 21 - Python)")
    print(f"Solution for part 1: {solution}")
