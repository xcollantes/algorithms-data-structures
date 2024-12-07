"""Unit test for rotate_array.py.

189. Rotate Array

Given an integer array nums, rotate the array to the right by k steps, where
k is non-negative.
"""

import unittest

from leetcode_questions.med.strings_arrays.rotate_array import rotate, rotate_group


class TestRotateArray(unittest.TestCase):
    def test_rotate_array(self):
        self.cases(rotate)

    def test_rotate_group_array(self):
        self.cases(rotate_group)

    def cases(self, fn):
        self.assertEqual(
            fn(nums=[0, 1, 2, 3, 4, 5, 6, 7], k=3), [5, 6, 7, 0, 1, 2, 3, 4]
        )
        self.assertEqual(fn(nums=[1, 2, 3, 4, 5, 6, 7], k=3), [5, 6, 7, 1, 2, 3, 4])
        self.assertEqual(fn(nums=[-1, -100, 3, 99], k=2), [3, 99, -1, -100])
        self.assertEqual(fn([1, 2], 3), [2, 1])
        self.assertEqual(fn([1, 2], 0), [1, 2])
