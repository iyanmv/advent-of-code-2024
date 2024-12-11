from pathlib import Path

module_path = Path(__file__).resolve().parent


def blink(list_stones):
    new_list = []
    for stone in list_stones:
        stone_str = str(stone)
        if stone == 0:
            new_list.append(1)
        elif len(stone_str) % 2 == 0:
            new_list.append(int(stone_str[: len(stone_str) // 2]))
            new_list.append(int(stone_str[len(stone_str) // 2 :]))
        else:
            new_list.append(2024 * stone)

    return new_list


def part_1(initial_string):
    list_stones = [int(n) for n in initial_string.split()]
    for _ in range(25):
        list_stones = blink(list_stones)

    return len(list_stones)


if __name__ == "__main__":
    with open(module_path / "input", "r") as file:
        stones = file.read().strip()

    solution = part_1(stones)

    print("Advent of Code 2024 (day 11 - Python)")
    print(f"Solution for part 1: {solution}")
