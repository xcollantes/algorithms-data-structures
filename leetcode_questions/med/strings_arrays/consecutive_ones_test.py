"""Unit test for consecutive_ones.py."""

import unittest
import logging

from leetcode_questions.med.strings_arrays.consecutive_ones import ones

logging.basicConfig(level=logging.INFO, format="%(message)s")


class TestConsecutiveOnes(unittest.TestCase):
    def test_consecutive_ones(self):
        self.assertEqual(ones(nums=[1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k=2), 6)
        self.assertEqual(
            ones(nums=[0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], k=3),
            10,
        )
