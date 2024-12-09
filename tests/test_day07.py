import sys
import unittest
from pathlib import Path

test_path = Path(__file__).resolve().parent

sys.path.append(str(test_path) + "/../solutions/day07")

from part1 import part_1
from part2 import part_2


class TestDay7(unittest.TestCase):
    def setUp(self):
        example = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""
        self.example = []
        for line in example.splitlines():
            target, numbers = line.split(":")
            target = int(target)
            numbers = [int(n) for n in numbers.split()]
            self.example.append((target, numbers))

    def test_example_part_1(self):
        self.assertEqual(part_1(self.example), 3749)

    def test_example_part_2(self):
        self.assertEqual(part_2(self.example), 11387)
