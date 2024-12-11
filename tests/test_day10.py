import sys
import unittest
from pathlib import Path

import numpy as np

test_path = Path(__file__).resolve().parent

sys.path.append(str(test_path) + "/../solutions/day10")

from part1 import part_1
from part2 import part_2


class TestDay10(unittest.TestCase):
    def setUp(self):
        example = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
"""
        self.example = np.array(
            [[n for n in line] for line in example.splitlines()], dtype=int
        )

    def test_example_part_1(self):
        self.assertEqual(part_1(self.example), 36)

    def test_example_part_2(self):
        self.assertEqual(part_2(self.example), 81)
