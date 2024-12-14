from pathlib import Path

import numpy as np

module_path = Path(__file__).resolve().parent


def parse_robots(text):
    robots = []
    for line in text.splitlines():
        pos, vel = line.split()
        x, y = map(int, pos[2:].split(","))
        vx, vy = map(int, vel[2:].split(","))
        robots.append({"pos": (x, y), "vel": (vx, vy)})
    return robots


def simulate(robots, size, rounds):
    final_map = np.zeros(size, dtype=int).T

    for robot in robots:
        x, y = robot["pos"]
        vx, vy = robot["vel"]
        final_x, final_y = (x + vx * rounds) % size[0], (y + vy * rounds) % size[1]
        final_map[final_y, final_x] += 1

    return final_map


def part_1(robots, size, rounds):
    robots_map = simulate(robots, size, rounds)
    rows, cols = robots_map.shape
    robots_per_cuadrant = []
    robots_per_cuadrant.append(robots_map[: rows // 2, : cols // 2].sum())
    robots_per_cuadrant.append(robots_map[: rows // 2, cols // 2 + 1 :].sum())
    robots_per_cuadrant.append(robots_map[rows // 2 + 1 :, : cols // 2].sum())
    robots_per_cuadrant.append(robots_map[rows // 2 + 1 :, cols // 2 + 1 :].sum())

    return np.prod(robots_per_cuadrant)


if __name__ == "__main__":
    with open(module_path / "input", "r") as file:
        initial_robots = parse_robots(file.read())

    solution = part_1(initial_robots, (101, 103), 100)

    print("Advent of Code 2024 (day 14 - Python)")
    print(f"Solution for part 1: {solution}")
