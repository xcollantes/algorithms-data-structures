"""Unit test for missing_num.py.

268. Missing Number

Find missing number.

Given an array nums containing n distinct numbers in the range [0, n], return
the only number in the range that is missing from the array.
"""

import unittest

from leetcode_questions.easy.strings_arrays.missing_num import (
    missing_num,
    optimized_missing_num,
)


class TestMissing(unittest.TestCase):
    def test_missing(self):
        self.assertEqual(missing_num([3, 0, 1]), 2)
        self.assertEqual(missing_num([0, 1]), 2)
        self.assertEqual(missing_num([9, 6, 4, 2, 3, 5, 7, 0, 1]), 8)

    def test_optimized(self):
        self.assertEqual(optimized_missing_num([3, 0, 1]), 2)
        self.assertEqual(optimized_missing_num([0, 1]), 2)
        self.assertEqual(optimized_missing_num([9, 6, 4, 2, 3, 5, 7, 0, 1]), 8)
