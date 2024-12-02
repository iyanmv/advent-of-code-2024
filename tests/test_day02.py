import sys
import unittest
from pathlib import Path

import numpy as np

test_path = Path(__file__).resolve().parent

sys.path.append(str(test_path) + "/../solutions/day02")

from part1 import part_1
from part2 import part_2


class TestDay2(unittest.TestCase):
    def setUp(self):
        example = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""
        example = example.splitlines()[1:]
        self.file_generator = (l for l in example)

    def test_example_part_1(self):
        self.assertEqual(part_1(self.file_generator), 2)

    def test_example_part_2(self):
        self.assertEqual(part_2(self.file_generator), 4)
