"""Unit test for two_sums.py."""

import unittest

from leetcode_questions.two_sums import two_sums


class TestTwoSums(unittest.TestCase):
    def test_twosums(self):
        self.assertEqual(two_sums([1, 2], 3), [0, 1])
        self.assertEqual(two_sums([2, 3, 5, 2, 14, 543, 23], 25), [0, 6])
        self.assertEqual(two_sums([56, 345, 0, 2, 4, 5], 2), [2, 3])
