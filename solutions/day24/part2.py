import secrets
from pathlib import Path
from itertools import combinations
from collections import Counter

import networkx as nx
import matplotlib.pyplot as plt

from part1 import parse_input, apply_op, part_1

module_path = Path(__file__).resolve().parent


def int_to_bits(n, n_bits):
    return f"{n:0{n_bits}b}"[::-1]


def bits_to_int(bits):
    out = 0
    for i, bit in enumerate(bits[::-1]):
        out += int(bit) << i
    return out


def get_bits_from_register(registers, letter):
    keys = sorted([key for key in registers.keys() if key.startswith(letter)])
    return "".join([str(registers[key]) for key in keys])


def prepare_register(x, y, n_bits):
    register = {}
    x_bits = int_to_bits(x, n_bits)
    y_bits = int_to_bits(y, n_bits)
    for i in range(n_bits):
        register[f"x{i:02d}"] = int(x_bits[i])
        register[f"y{i:02d}"] = int(y_bits[i])
    return register


def check_register(z, registers, n_bits):
    z_bits = f"{z:0{n_bits}b}"[::-1]
    keys = sorted([key for key in registers.keys() if key.startswith("z")])
    z = "".join([str(registers[key]) for key in keys])
    if len(z) == len(z_bits) - 1:
        z += "0"
    else:
        raise ValueError("Wrong number of bits")
    if z == z_bits:
        return True
    return False


def modify_operations(operations, swap):
    new_operations = operations.copy()
    for a, b in swap:
        for i, op1 in enumerate(operations):
            if op1[3] == a:
                a = i
                for j, op2 in enumerate(operations):
                    if op2[3] == b:
                        b = j
                        break
                else:
                    continue
                break
        # fmt: off
        new_operations[a] = (operations[a][0], operations[a][1], operations[a][2], operations[b][3])
        new_operations[b] = (operations[b][0], operations[b][1], operations[b][2], operations[a][3])
        # fmt: on
    return new_operations


def generate_graph(operations):
    graph = nx.DiGraph()
    counter = Counter()
    for op in operations:
        op_name = op[0] + f"_{counter[op[0]]}"
        graph.add_edge(op[1], op_name)
        graph.add_edge(op[2], op_name)
        graph.add_edge(op_name, op[3])
        counter[op[0]] += 1
    return graph


def part_2(operations):
    graph = generate_graph(operations)
    nx.nx_agraph.to_agraph(graph).draw("operations_ori.pdf", prog="dot")
    # Manual inspection for weird gates
    # TODO: automatize this somehow
    swaps = [("hdt", "z05"), ("z09", "gbf"), ("mht", "jgt"), ("z30", "nbf")]
    new_operations = modify_operations(operations, swaps)
    graph = generate_graph(new_operations)
    nx.nx_agraph.to_agraph(graph).draw("operations_updated.pdf", prog="dot")
    solution = []
    for a, b in swaps:
        solution.append(a)
        solution.append(b)

    return ",".join(sorted(solution))


if __name__ == "__main__":
    with open(module_path / "input", "r") as file:
        registers, operations = parse_input(file.read())

    solution = part_2(operations)

    print("Advent of Code 2024 (day 24 - Python)")
    print(f"Solution for part 2: {solution}")
