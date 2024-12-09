import sys
import unittest
from pathlib import Path

import numpy as np

test_path = Path(__file__).resolve().parent

sys.path.append(str(test_path) + "/../solutions/day05")

from part1 import part_1
from part2 import part_2


class TestDay5(unittest.TestCase):
    def setUp(self):
        rules = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13"""
        self.rules = np.loadtxt(rules.splitlines(), delimiter="|", dtype=int)
        updates = """75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""
        self.updates = [
            [int(num) for num in line.split(",")] for line in updates.splitlines()
        ]

    def test_example_part_1(self):
        self.assertEqual(part_1(self.rules, self.updates), 143)

    def test_example_part_2(self):
        self.assertEqual(part_2(self.rules, self.updates), 123)
