from pathlib import Path

module_path = Path(__file__).resolve().parent


def parse_input(text):
    regs, opers = text.split("\n\n")

    registers = {}
    for line in regs.splitlines():
        reg, val = line.split(":")
        registers[reg] = int(val)

    operations = []
    for line in opers.splitlines():
        # fmt: off
        x, op, y, _, z, = line.split(" ")
        # fmt: on
        operations.append((op, x, y, z))

    return registers, operations


def apply_op(op, x, y):
    if op == "AND":
        return x and y
    elif op == "OR":
        return x or y
    elif op == "XOR":
        return x ^ y
    else:
        raise ValueError("Unknown op")


def get_result(registers):
    keys = sorted([key for key in registers.keys() if key.startswith("z")])
    result = 0
    for i, key in enumerate(keys):
        result += registers[key] << i
    return result


def part_1(registers, operations):
    pending = operations.copy()
    while len(pending) > 0:
        for instruction in pending:
            op, in1, in2, out = instruction
            if in1 not in registers or in2 not in registers:
                continue
            registers[out] = apply_op(op, registers[in1], registers[in2])
            pending.remove(instruction)
    return get_result(registers)


if __name__ == "__main__":
    with open(module_path / "input", "r") as file:
        registers, operations = parse_input(file.read())

    solution = part_1(registers, operations)

    print("Advent of Code 2024 (day 24 - Python)")
    print(f"Solution for part 1: {solution}")
