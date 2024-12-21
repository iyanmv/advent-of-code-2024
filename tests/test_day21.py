import sys
import unittest
from pathlib import Path

test_path = Path(__file__).resolve().parent

sys.path.append(str(test_path) + "/../solutions/day21")

from part1 import part_1
from part2 import part_2


class TestDay21(unittest.TestCase):
    def setUp(self):
        example = """029A
980A
179A
456A
379A
"""
        self.example = example.splitlines()

    def test_example_part_1(self):
        self.assertEqual(part_1(self.example), 126384)

    def test_example_part_2(self):
        self.assertEqual(part_2(self.example, 2), 126384)
