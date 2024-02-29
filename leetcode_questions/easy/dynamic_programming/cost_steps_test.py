"""Unit test for cost_steps.py."""

import unittest
import logging

from leetcode_questions.easy.dynamic_programming.cost_steps import min_cost

logging.basicConfig(level=logging.INFO, format="%(message)s")


class TestCostSteps(unittest.TestCase):
    def test_cost_steps(self):
        self.assertEqual(min_cost([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]), 6)

    def test_cost_steps_three(self):
        self.assertEqual(min_cost([10, 15, 20]), 15)
