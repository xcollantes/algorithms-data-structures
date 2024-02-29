"""Unit test for coins.py."""

import unittest
import logging

from leetcode_questions.med.dynamic_programming.coins import coin

logging.basicConfig(level=logging.INFO, format="%(message)s")


class TestCoins(unittest.TestCase):
    def test_coins(self):
        self.assertEqual(coin([1, 2, 5], 11), 3)
        self.assertEqual(coin([2], 3), -1)
        self.assertEqual(coin([1], 0), 0)
