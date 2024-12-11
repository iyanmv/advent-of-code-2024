from pathlib import Path

module_path = Path(__file__).resolve().parent


def blink_alt(stones):
    new_stones = dict()

    for number, count in stones.items():
        half, is_odd = divmod(len(str(number)), 2)
        number_str = str(number)

        if number == 0:
            if 1 not in new_stones:
                new_stones[1] = count
            else:
                new_stones[1] += count
        elif is_odd:
            if number * 2024 not in new_stones:
                new_stones[number * 2024] = count
            else:
                new_stones[number * 2024] += count
        else:
            left = int(number_str[:half])
            right = int(number_str[half:])
            if left not in new_stones:
                new_stones[left] = count
            else:
                new_stones[left] += count
            if right not in new_stones:
                new_stones[right] = count
            else:
                new_stones[right] += count

    return new_stones


def part_2(initial_string):
    dict_stones = dict([int(n), 1] for n in initial_string.split())
    for _ in range(75):
        dict_stones = blink_alt(dict_stones)

    return sum(dict_stones.values())


if __name__ == "__main__":
    with open(module_path / "input", "r") as file:
        stones = file.read().strip()

    solution = part_2(stones)

    print("Advent of Code 2024 (day 11 - Python)")
    print(f"Solution for part 2: {solution}")
