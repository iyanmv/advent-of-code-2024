from pathlib import Path
from math import floor

module_path = Path(__file__).resolve().parent


def parse_program(text):
    registers, instructions = text.split("\n\n")
    registers = [int(line.split(":")[1]) for line in registers.splitlines()]
    registers = dict([(l, n) for l, n in zip(["A", "B", "C"], registers)])
    instructions = instructions.split(":")[1]
    instructions = [int(n) for n in instructions.split(",")]
    program = {"point": 0, "ins": instructions}
    return registers, program


def combo_operand(operand, registers):
    if operand < 4:
        return operand
    elif operand == 4:
        return registers["A"]
    elif operand == 5:
        return registers["B"]
    elif operand == 6:
        return registers["C"]
    else:
        raise ValueError(f"Invalid combo operand: {operand}")


def adv(operand, registers, program):
    operand = combo_operand(operand, registers)
    registers["A"] = floor(registers["A"] / 2**operand)
    program["point"] += 2


def bxl(operand, registers, program):
    registers["B"] = operand ^ registers["B"]
    program["point"] += 2


def bst(operand, registers, program):
    operand = combo_operand(operand, registers)
    registers["B"] = operand % 8
    program["point"] += 2


def jnz(operand, registers, program):
    if registers["A"] == 0:
        program["point"] += 2
        return
    program["point"] = operand


def bxc(operand, registers, program):
    registers["B"] ^= registers["C"]
    program["point"] += 2


def out(operand, registers, program):
    operand = combo_operand(operand, registers)
    program["point"] += 2
    return operand % 8


def bdv(operand, registers, program):
    operand = combo_operand(operand, registers)
    registers["B"] = floor(registers["A"] / 2**operand)
    program["point"] += 2


def cdv(operand, registers, program):
    operand = combo_operand(operand, registers)
    registers["C"] = floor(registers["A"] / 2**operand)
    program["point"] += 2


def exec_ins(opcode, operand, registers, program):
    if opcode == 0:
        return adv(operand, registers, program)
    elif opcode == 1:
        return bxl(operand, registers, program)
    elif opcode == 2:
        return bst(operand, registers, program)
    elif opcode == 3:
        return jnz(operand, registers, program)
    elif opcode == 4:
        return bxc(operand, registers, program)
    elif opcode == 5:
        return out(operand, registers, program)
    elif opcode == 6:
        return bdv(operand, registers, program)
    elif opcode == 7:
        return cdv(operand, registers, program)
    else:
        raise ValueError(f"Invalid opcode: {opcode}")


def part_1(registers, program):
    output = []
    while program["point"] < len(program["ins"]) - 1:
        pointer = program["point"]
        opcode, operand = program["ins"][pointer], program["ins"][pointer + 1]
        out = exec_ins(opcode, operand, registers, program)
        if out is not None:
            output.append(str(out))
    return ",".join(output)


if __name__ == "__main__":
    with open(module_path / "input", "r") as file:
        registers, program = parse_program(file.read())

    solution = part_1(registers, program)

    print("Advent of Code 2024 (day 17 - Python)")
    print(f"Solution for part 1: {solution}")
