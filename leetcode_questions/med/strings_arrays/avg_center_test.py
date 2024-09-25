"""Unit test for avg_center.py.

You are given a 0-indexed array nums of n integers, and an integer k.

The k-radius average for a subarray of nums centered at some index i with the
radius k is the average of all elements in nums between the indices i - k and i
+ k (inclusive). If there are less than k elements before or after the index i,
then the k-radius average is -1.

Build and return an array avgs of length n where avgs[i] is the k-radius average
for the subarray centered at index i.

The average of x elements is the sum of the x elements divided by x, using
integer division. The integer division truncates toward zero, which means losing
its fractional part.

For example, the average of four elements 2, 3, 1, and 5 is (2 + 3 + 1 + 5) / 4
= 11 / 4 = 2.75, which truncates to 2.
"""

import logging
import unittest

from leetcode_questions.med.strings_arrays.avg_center import (avg_center,
                                                              faster_avg)

logging.basicConfig(level=logging.INFO, format="%(message)s")


class TestAvgCenter(unittest.TestCase):
    def test_avg_center(self):
        self.cases(avg_center)

    def test_faster(self):
        self.cases(faster_avg)

    def cases(self, fn):
        self.assertEqual(fn([2, 1, 3, 1, 0, 2, 1], 2), [-1, -1, 1, 1, 1, -1, -1])
        self.assertEqual(
            fn([7, 4, 3, 9, 1, 8, 5, 2, 6], 3),
            [-1, -1, -1, 5, 4, 4, -1, -1, -1],
        )
        self.assertEqual(fn([100000], 0), [100000])
        self.assertEqual(fn([8], 100000), [-1])
