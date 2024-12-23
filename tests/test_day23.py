import sys
import unittest
from pathlib import Path

test_path = Path(__file__).resolve().parent

sys.path.append(str(test_path) + "/../solutions/day23")

from part1 import part_1, parse_computers
from part2 import part_2


class TestDay23(unittest.TestCase):
    def setUp(self):
        example = """kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn
"""
        self.example = parse_computers(example)


    def test_example_part_1(self):
        self.assertEqual(part_1(self.example), 7)

    def test_example_part_2(self):
        self.assertEqual(part_2(self.example), "co,de,ka,ta")
