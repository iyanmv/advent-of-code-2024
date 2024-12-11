import sys
import unittest
from pathlib import Path

import numpy as np

test_path = Path(__file__).resolve().parent

sys.path.append(str(test_path) + "/../solutions/day08")

from part1 import part_1
from part2 import part_2


class TestDay8(unittest.TestCase):
    def setUp(self):
        example = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""
        self.example = np.array(
            [[letter for letter in line] for line in example.splitlines()]
        )

        example_2 = """T.........
...T......
.T........
..........
..........
..........
..........
..........
..........
..........
"""
        self.example_2 = np.array(
            [[letter for letter in line] for line in example_2.splitlines()]
        )

    def test_example_part_1(self):
        self.assertEqual(part_1(self.example), 14)

    def test_example_part_2(self):
        self.assertEqual(part_2(self.example_2), 9)
        self.assertEqual(part_2(self.example), 34)