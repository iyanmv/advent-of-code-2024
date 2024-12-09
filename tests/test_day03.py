import sys
import unittest
from pathlib import Path

test_path = Path(__file__).resolve().parent

sys.path.append(str(test_path) + "/../solutions/day03")

from part1 import part_1
from part2 import part_2


class TestDay3(unittest.TestCase):
    def setUp(self):
        self.example_1 = (
            "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
        )
        self.example_2 = (
            "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
        )

    def test_example_part_1(self):
        self.assertEqual(part_1(self.example_1), 161)

    def test_example_part_2(self):
        self.assertEqual(part_2(self.example_2), 48)
