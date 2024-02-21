"""Unit test for avg_center.py."""

import unittest
import logging

from leetcode_questions.med.avg_center import avg_center, faster_avg

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
