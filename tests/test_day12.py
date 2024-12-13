import sys
import unittest
from pathlib import Path

import numpy as np

test_path = Path(__file__).resolve().parent

sys.path.append(str(test_path) + "/../solutions/day12")

from part1 import part_1
from part2 import part_2


class TestDay12(unittest.TestCase):
    def setUp(self):
        example_1 = """AAAA
BBCD
BBCC
EEEC
"""
        self.example_1 = np.array(
            [[l for l in line] for line in example_1.splitlines()]
        )
        example_2 = """OOOOO
OXOXO
OOOOO
OXOXO
OOOOO
"""
        self.example_2 = np.array(
            [[l for l in line] for line in example_2.splitlines()]
        )

        example_3 = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
"""
        self.example_3 = np.array(
            [[l for l in line] for line in example_3.splitlines()]
        )

    def test_examples_part_1(self):
        self.assertEqual(part_1(self.example_1), 140)
        self.assertEqual(part_1(self.example_2), 772)
        self.assertEqual(part_1(self.example_3), 1930)

    def test_examples_part_2(self):
        self.assertEqual(part_2(self.example_1), 80)
        self.assertEqual(part_2(self.example_2), 436)
        self.assertEqual(part_2(self.example_3), 1206)
