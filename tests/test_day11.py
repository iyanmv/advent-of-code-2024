import sys
import unittest
from pathlib import Path

import numpy as np

test_path = Path(__file__).resolve().parent

sys.path.append(str(test_path) + "/../solutions/day11")

from part1 import part_1


class TestDay11(unittest.TestCase):
    def setUp(self):
        self.example = "125 17"

    def test_example_part_1(self):
        self.assertEqual(part_1(self.example), 55312)
