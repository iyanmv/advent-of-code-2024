from pathlib import Path

import numpy as np

module_path = Path(__file__).resolve().parent


def parse_robots(text):
    robots = []
    for line in text.splitlines():
        pos, vel = line.split()
        y, x = map(int, pos[2:].split(","))
        vy, vx = map(int, vel[2:].split(","))
        robots.append({"pos": (x, y), "vel": (vx, vy)})
    return robots


def part_1(robots, size, rounds):
    final_map = np.zeros(size, dtype=int)

    for robot in robots:
        x, y = robot["pos"]
        vx, vy = robot["vel"]
        final_x, final_y = (x + vx * rounds) % size[0], (y + vy * rounds) % size[1]
        final_map[final_x, final_y] += 1

    robots_per_cuadrant = []
    robots_per_cuadrant.append(final_map[: size[0] // 2, : size[1] // 2].sum())
    robots_per_cuadrant.append(final_map[: size[0] // 2, size[1] // 2 + 1 :].sum())
    robots_per_cuadrant.append(final_map[size[0] // 2 + 1 :, : size[1] // 2].sum())
    robots_per_cuadrant.append(final_map[size[0] // 2 + 1 :, size[1] // 2 + 1 :].sum())

    return np.prod(robots_per_cuadrant)


if __name__ == "__main__":
    with open(module_path / "input", "r") as file:
        initial_robots = parse_robots(file.read())

    solution = part_1(initial_robots, (103, 101), 100)

    print("Advent of Code 2024 (day 14 - Python)")
    print(f"Solution for part 1: {solution}")
