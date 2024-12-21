from itertools import product
from pathlib import Path

import networkx as nx

from part1 import generate_numeric_pad, generate_keypad

module_path = Path(__file__).resolve().parent


def get_all_sequences(curr_pos, seq, pad, known_paths):
    directions = {(0, -1): "<", (0, 1): ">", (-1, 0): "^", (1, 0): "v"}
    sym_to_pos, pos_to_sym, graph = pad
    sequences = []

    for i in range(len(seq)):
        next_sym = seq[i]
        next_pos = sym_to_pos[next_sym]
        if (curr_pos, next_pos) in known_paths:
            paths = known_paths[(curr_pos, next_pos)]
        else:
            paths = list(nx.all_shortest_paths(graph, curr_pos, next_pos))
            known_paths[(curr_pos, next_pos)] = paths

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

    min_seq = len(min(sequences, key=len))
    final_seqs = [s for s in sequences if len(s) == min_seq]
    return final_seqs


def precompute_keypad_seqs(keypad):
    sym_to_pos, pos_to_sym, _ = keypad
    buttons = ["<", ">", "^", "v", "A"]
    seqs = {}
    for curr_pos, next_pos in product(buttons, buttons):
        seq = (curr_pos, next_pos)
        seqs[seq] = get_all_sequences(sym_to_pos[curr_pos], next_pos, keypad, {})
    return seqs


def compute_length_seq(seq, keypad_seqs, keypad_seqs_lengths, depth, memory):
    if (seq, depth) in memory:
        return memory[(seq, depth)]

    if depth == 1:
        sol = sum(keypad_seqs_lengths[(a, b)] for a, b in zip("A" + seq, seq))
        memory[(seq, depth)] = sol
        return sol

    length = 0
    for a, b in zip("A" + seq, seq):
        length += min(compute_length_seq(s, keypad_seqs, keypad_seqs_lengths, depth - 1, memory) for s in keypad_seqs[(a, b)])
    memory[(seq, depth)] = length
    return length


def part_2(pins, n_dir_keypads):
    numpad = generate_numeric_pad()
    keypad = generate_keypad()

    keypad_seqs = precompute_keypad_seqs(keypad)
    keypad_seqs_lengths = {key: len(val[0]) for key, val in keypad_seqs.items()}
    known_paths_numpad = {}
    memory = {}

    solution = 0
    for pin in pins:
        robot_num_seqs = get_all_sequences((3, 2), pin, numpad, known_paths_numpad)
        lengths = [compute_length_seq(s, keypad_seqs, keypad_seqs_lengths, n_dir_keypads, memory) for s in robot_num_seqs]
        solution += min(lengths) * int(pin[:-1])

    return solution


if __name__ == "__main__":
    with open(module_path / "input", "r") as file:
        pins = file.read().splitlines()

    solution = part_2(pins, 25)

    print("Advent of Code 2024 (day 21 - Python)")
    print(f"Solution for part 2: {solution}")
