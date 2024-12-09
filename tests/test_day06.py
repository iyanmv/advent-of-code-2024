import sys
import unittest
from pathlib import Path

import numpy as np

test_path = Path(__file__).resolve().parent

sys.path.append(str(test_path) + "/../solutions/day06")

from part1 import part_1
from part2 import part_2


class TestDay6(unittest.TestCase):
    def setUp(self):
        example = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""
        self.example = np.array(
            [[letter for letter in line] for line in example.splitlines()]
        )

    def test_example_part_1(self):
        self.assertEqual(part_1(self.example), 41)

    def test_example_part_2(self):
        self.assertEqual(part_2(self.example), 6)
