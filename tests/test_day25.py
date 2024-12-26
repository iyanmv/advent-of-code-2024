import sys
import unittest
from pathlib import Path

test_path = Path(__file__).resolve().parent

sys.path.append(str(test_path) + "/../solutions/day25")

from part1 import parse_input, part_1


class TestDay25(unittest.TestCase):
    def setUp(self):
        example_1 = """#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####
"""
        self.example_1 = parse_input(example_1)

    def test_example_part_1(self):
        self.assertEqual(part_1(*self.example_1), 3)
