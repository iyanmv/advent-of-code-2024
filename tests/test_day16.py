import sys
import unittest
from pathlib import Path

test_path = Path(__file__).resolve().parent

sys.path.append(str(test_path) + "/../solutions/day16")

from part1 import part_1, parse_maze
from part2 import part_2


class TestDay16(unittest.TestCase):
    def setUp(self):
        example_1 = """###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############
"""
        self.example_1 = parse_maze(example_1)

        example_2 = """#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################
"""
        self.example_2 = parse_maze(example_2)

    def test_examples_part_1(self):
        self.assertEqual(part_1(self.example_1), 7036)
        self.assertEqual(part_1(self.example_2), 11048)

    def test_examples_part_2(self):
        self.assertEqual(part_2(self.example_1), 45)
        self.assertEqual(part_2(self.example_2), 64)
