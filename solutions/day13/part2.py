from pathlib import Path

from part1 import parse_game

module_path = Path(__file__).resolve().parent


def part_2(games):
    wins = 0
    tokens = []

    for game in games:
        Ax, Ay = game["A"]
        Bx, By = game["B"]
        X, Y = [n + 10**13 for n in game["Prize"]]
        B = (Ax * Y - Ay * X) // (Ax * By - Ay * Bx)
        A = (X - Bx * B) // Ax
        if Ax * A + Bx * B == X and Ay * A + By * B == Y:
            wins += 1
            tokens.append(3 * A + B)

    return sum(tokens)


if __name__ == "__main__":
    with open(module_path / "input", "r") as file:
        games = parse_game(file.read())

    solution = part_2(games)

    print("Advent of Code 2024 (day 13 - Python)")
    print(f"Solution for part 2: {solution}")
