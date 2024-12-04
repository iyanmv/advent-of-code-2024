import sys
import unittest
from pathlib import Path

import numpy as np

test_path = Path(__file__).resolve().parent

sys.path.append(str(test_path) + "/../solutions/day04")

from part1 import part_1
from part2 import part_2


class TestDay2(unittest.TestCase):
    def setUp(self):
        example = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""
        text = []
        for line in example.splitlines():
            text.append([l for l in line.strip()])
        self.array = np.array(text)

    def test_example_part_1(self):
        self.assertEqual(part_1(self.array), 18)

    def test_example_part_2(self):
        self.assertEqual(part_2(self.array), 9)
