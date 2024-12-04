import re
from pathlib import Path

module_path = Path(__file__).resolve().parent


def part_2(string):
    pattern = r"do\(\)|don't\(\)|mul\([0-9]{1,3},[0-9]{1,3}\)"
    regex_expr = re.compile(pattern)

    result = 0
    enabled = True

    for match in re.finditer(regex_expr, string):
        if match.group(0) == "do()":
            enabled = True
            continue
        if match.group(0) == "don't()":
            enabled = False
            continue
        if enabled:
            numbers = [int(_) for _ in match.group(0)[4:-1].split(",")]
            result += numbers[0] * numbers[1]

    return result


if __name__ == "__main__":
    with open(module_path / "input", "r") as file:
        text = file.read()

    solution = part_2(text)

    print("Advent of Code 2024 (day 3 - Python)")
    print(f"Solution for part 2: {solution}")
