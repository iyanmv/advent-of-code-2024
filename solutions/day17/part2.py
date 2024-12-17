from pathlib import Path

from part1 import exec_ins, parse_program

module_path = Path(__file__).resolve().parent


def part_2(registers, program):
    registers_ori = registers.copy()
    count = 0
    n_found = 1
    while True:
        program["point"] = 0
        registers = registers_ori.copy()
        registers["A"] = count
        output = []
        while program["point"] < len(program["ins"]) - 1:
            pointer = program["point"]
            opcode, operand = program["ins"][pointer], program["ins"][pointer + 1]
            out = exec_ins(opcode, operand, registers, program)
            if out is not None:
                output.append(out)

        if output == program["ins"]:
            return count
        elif output == program["ins"][len(program["ins"]) - n_found :]:
            count *= 8
            n_found += 1
        else:
            count += 1


if __name__ == "__main__":
    with open(module_path / "input", "r") as file:
        registers, program = parse_program(file.read())

    solution = part_2(registers, program)

    print("Advent of Code 2024 (day 17 - Python)")
    print(f"Solution for part 2: {solution}")
