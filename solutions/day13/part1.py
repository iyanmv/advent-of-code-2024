from pathlib import Path

import numpy as np
import scipy as sp
from scipy.optimize import milp, Bounds, LinearConstraint

module_path = Path(__file__).resolve().parent


def parse_game(text):
    games = []
    game = dict()
    for line in text.splitlines():
        parts = line.split()

        if len(parts) == 0:
            games.append(game)
            game = dict()
            continue

        if parts[0] == "Button":
            steps = (int(parts[2][2:-1]), int(parts[3][2:]))
            if parts[1] == "A:":
                game["A"] = steps
            elif parts[1] == "B:":
                game["B"] = steps
        elif parts[0] == "Prize:":
            game["Prize"] = (int(parts[1][2:-1]), int(parts[2][2:]))

    games.append(game)
    return games


def part_1(games):
    wins = 0
    tokens = []
    c = np.array([3, 1], dtype=int)
    integrality = np.array([3, 3], dtype=int)
    bounds = Bounds(lb=0, ub=100)
    for game in games:
        A = np.array([game["A"], game["B"]], dtype=int).T
        b = np.array(game["Prize"])
        constraint = LinearConstraint(A, lb=b, ub=b)
        res = milp(c, integrality=integrality, bounds=bounds, constraints=constraint)
        if res.success:
            wins += 1
            tokens.append(int(res.mip_dual_bound))

    return sum(tokens)


if __name__ == "__main__":
    with open(module_path / "input", "r") as file:
        games = parse_game(file.read())

    solution = part_1(games)

    print("Advent of Code 2024 (day 13 - Python)")
    print(f"Solution for part 1: {solution}")
