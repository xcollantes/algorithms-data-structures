"""Unit test for avg_center.py."""

import unittest
import logging

from leetcode_questions.med.avg_center import avg_center

logging.basicConfig(level=logging.INFO, format="%(message)s")


class TestAvgCenter(unittest.TestCase):
    def test_avg_center(self):
        self.assertEqual(
            avg_center([2, 1, 3, 1, 0, 2, 1], 2), [-1, -1, 1, 1, 1, -1, -1]
        )
        self.assertEqual(
            avg_center([7, 4, 3, 9, 1, 8, 5, 2, 6], 3),
            [-1, -1, -1, 5, 4, 4, -1, -1, -1],
        )
        self.assertEqual(avg_center([100000], 0), [100000])
        self.assertEqual(avg_center([8], 100000), [-1])
