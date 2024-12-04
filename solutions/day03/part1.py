import re
from pathlib import Path

module_path = Path(__file__).resolve().parent


def part_1(string):
    pattern = r"mul\(([0-9]{1,3}),([0-9]{1,3})\)"
    regex_expr = re.compile(pattern)
    return sum([int(_[0]) * int(_[1]) for _ in re.findall(regex_expr, string)])


if __name__ == "__main__":
    with open(module_path / "input", "r") as file:
        text = file.read()

    solution = part_1(text)

    print("Advent of Code 2024 (day 3 - Python)")
    print(f"Solution for part 1: {solution}")
