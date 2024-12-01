import sys
import unittest
from pathlib import Path

import numpy as np

test_path = Path(__file__).resolve().parent

sys.path.append(str(test_path) + "/../solutions/day01")

from part1 import part_1
from part2 import part_2


class TestDay1(unittest.TestCase):
    def setUp(self):
        list_1 = [3, 4, 2, 1, 3, 3]
        list_2 = [4, 3, 5, 3, 9, 3]
        self.arr = np.array([list_1, list_2]).T

    def test_example_part_1(self):
        self.assertEqual(part_1(self.arr), 11)

    def test_example_part_2(self):
        self.assertEqual(part_2(self.arr), 31)
