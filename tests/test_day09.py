import sys
import unittest
from pathlib import Path

test_path = Path(__file__).resolve().parent

sys.path.append(str(test_path) + "/../solutions/day09")

from part1 import part_1
from part2 import part_2


class TestDay9(unittest.TestCase):
    def setUp(self):
        self.example = "2333133121414131402"

    def test_example_part_1(self):
        self.assertEqual(part_1(self.example), 1928)

    def test_example_part_2(self):
        self.assertEqual(part_2(self.example), 2858)
