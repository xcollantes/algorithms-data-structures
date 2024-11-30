"""Unit test for coins.py.

322. Coin Change

Medium

You are given an integer array coins representing coins of different
denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that
amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
"""

import unittest

from leetcode_questions.med.dynamic_programming.coins import coin


class TestCoins(unittest.TestCase):
    def test_coins(self):
        self.assertEqual(coin([1, 2, 5], 11), 3)
        self.assertEqual(coin([2], 3), -1)
        self.assertEqual(coin([1], 0), 0)
