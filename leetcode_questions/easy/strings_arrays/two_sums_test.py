"""Unit test for two_sums.py."""

import unittest

from leetcode_questions.easy.strings_arrays.two_sums import faster_two_sums, two_sums


class TestTwoSums(unittest.TestCase):

    def cases(self, fn):
        self.assertEqual(fn([1, 2], 3), [0, 1])
        self.assertEqual(fn([2, 3, 5, 14, 543, 23], 25), [0, 5])
        self.assertEqual(fn([56, 345, 0, 2, 4, 5], 2), [2, 3])

    def test_twosums(self):
        self.cases(two_sums)

    def test_faster_two_sums(self):
        self.cases(faster_two_sums)
