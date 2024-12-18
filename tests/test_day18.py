import sys
import unittest
from pathlib import Path

test_path = Path(__file__).resolve().parent

sys.path.append(str(test_path) + "/../solutions/day18")

from part1 import part_1, parse_memory
from part2 import part_2, parse_bytes


class TestDay18(unittest.TestCase):
    def setUp(self):
        self.example = """5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0
"""

    def test_example_part_1(self):
        memory = parse_memory(self.example, 12, (7, 7))
        self.assertEqual(part_1(memory), 22)

    def test_example_part_2(self):
        corrupted_bytes = parse_bytes(self.example)
        self.assertEqual(part_2(corrupted_bytes, (7, 7)), "6,1")
