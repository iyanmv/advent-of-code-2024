import sys
import unittest
from pathlib import Path

test_path = Path(__file__).resolve().parent

sys.path.append(str(test_path) + "/../solutions/day17")

from part1 import part_1, parse_program
from part2 import part_2


class TestDay17(unittest.TestCase):
    def setUp(self):
        example_1 = """Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0
"""
        self.example_1 = parse_program(example_1)

        example_2 = """Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0
"""
        self.example_2 = parse_program(example_2)

    def test_example_part_1(self):
        self.assertEqual(part_1(*self.example_1), "4,6,3,5,6,3,5,2,1,0")

    def test_example_part_2(self):
        self.assertEqual(part_2(*self.example_2), 117440)
