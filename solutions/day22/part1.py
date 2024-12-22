from pathlib import Path


module_path = Path(__file__).resolve().parent


def get_next_number(n):
    a = n * 64
    a ^= n
    n = a % 16777216
    a = int(n // 32)
    a ^= n
    n = a % 16777216
    a = n * 2048
    a ^= n
    n = a % 16777216
    return n


def part_1(nums):
    solution = 0
    for n in nums:
        for _ in range(2000):
            n = get_next_number(n)
        solution += n
    return solution


if __name__ == "__main__":
    with open(module_path / "input", "r") as file:
        nums = map(int, file.read().splitlines())

    solution = part_1(nums)

    print("Advent of Code 2024 (day 22 - Python)")
    print(f"Solution for part 1: {solution}")
