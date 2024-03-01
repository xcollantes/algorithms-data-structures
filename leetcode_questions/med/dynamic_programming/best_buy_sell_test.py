"""Unit test for best_buy_sell.py."""

import unittest
import logging

from leetcode_questions.med.dynamic_programming.best_buy_sell import max_profit

logging.basicConfig(level=logging.INFO, format="%(message)s")


class TestBestBuySell(unittest.TestCase):
    def test_best_buy_sell(self):
        self.assertEqual(
            max_profit([1, 3, 2, 8, 4, 9], 2),
            8,
        )
        self.assertEqual(
            max_profit([1, 3, 7, 5, 10, 3], 3),
            6,
        )
