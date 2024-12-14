import sys
import unittest
from pathlib import Path

import numpy as np

test_path = Path(__file__).resolve().parent

sys.path.append(str(test_path) + "/../solutions/day14")

from part1 import part_1, parse_robots


class TestDay14(unittest.TestCase):
    def setUp(self):
        example = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3
"""
        self.example = parse_robots(example)

    def test_examples_part_1(self):
        self.assertEqual(
            part_1(self.example, (11, 7), 100),
            12,
        )
