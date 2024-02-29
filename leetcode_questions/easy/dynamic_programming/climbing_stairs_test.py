"""Unit test for climbing_stairs.py."""

import unittest
import logging

from leetcode_questions.easy.dynamic_programming.climbing_stairs import climb

logging.basicConfig(level=logging.INFO, format="%(message)s")


class TestClimbingStairs(unittest.TestCase):
    def test_climbing_stairs(self):
        self.assertEqual(climb(2), 2)
        self.assertEqual(climb(3), 3)
        self.assertEqual(climb(10), 10)
