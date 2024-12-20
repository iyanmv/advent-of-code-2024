import sys
import unittest
from pathlib import Path

test_path = Path(__file__).resolve().parent

sys.path.append(str(test_path) + "/../solutions/day20")

from part1 import part_1, parse_map
from part2 import part_2


class TestDay20(unittest.TestCase):
    def setUp(self):
        example = """###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
"""
        self.example = parse_map(example)

    def test_example_part_1(self):
        solution = part_1(self.example, 2)
        self.assertEqual(solution, {2:14, 4:14, 6:2, 8:4, 10:2, 12:3, 20:1, 36:1, 38:1, 40:1, 64:1})
        self.assertEqual(sum(solution.values()), 44)

    def test_example_part_2(self):
        solution = part_2(self.example, 50, 20)
        self.assertEqual(
            solution,
            {50:32, 52:31, 54:29, 56:39, 58:25, 60:23, 62:20, 64:19, 66:12, 68:14, 70:12, 72:22, 74:4, 76:3}
        )
        self.assertEqual(sum(solution.values()), 285)
