import sys
import unittest
from pathlib import Path

test_path = Path(__file__).resolve().parent

sys.path.append(str(test_path) + "/../solutions/day19")

from part1 import part_1, parse_towels
from part2 import part_2


class TestDay19(unittest.TestCase):
    def setUp(self):
        self.example = """r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb
"""

    def test_example_part_1(self):
        towels, patterns = parse_towels(self.example)
        self.assertEqual(part_1(towels, patterns), 6)

    def test_example_part_2(self):
        towels, patterns = parse_towels(self.example)
        self.assertEqual(part_2(towels, patterns), 16)