import sys
import unittest
from pathlib import Path

import numpy as np

test_path = Path(__file__).resolve().parent

sys.path.append(str(test_path) + "/../solutions/day13")

from part1 import part_1, parse_game
from part2 import part_2


class TestDay13(unittest.TestCase):
    def setUp(self):
        example = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
"""
        self.example = parse_game(example)

    def test_examples_part_1(self):
        self.assertEqual(part_1(self.example), 480)

    def test_examples_part_2(self):
        self.assertEqual(part_2(self.example), 875318608908)
