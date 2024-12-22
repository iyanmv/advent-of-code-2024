import sys
import unittest
from pathlib import Path

test_path = Path(__file__).resolve().parent

sys.path.append(str(test_path) + "/../solutions/day22")

from part1 import part_1
from part2 import part_2


class TestDay22(unittest.TestCase):
    def setUp(self):
        example_1 = """1
10
100
2024
"""
        self.example_1 = map(int, example_1.splitlines())

        example_2 = """1
2
3
2024
"""
        self.example_2 = map(int, example_2.splitlines())

    def test_example_part_1(self):
        self.assertEqual(part_1(self.example_1), 37327623)

    def test_example_part_2(self):
        self.assertEqual(part_2(self.example_2), ((-2, 1, -1, 3), 23))
