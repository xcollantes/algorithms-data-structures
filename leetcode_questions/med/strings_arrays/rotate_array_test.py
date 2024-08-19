"""Unit test for rotate_array.py."""

import unittest
import logging

from leetcode_questions.med.strings_arrays.rotate_array import rotate, rotate_group

logging.basicConfig(level=logging.INFO, format="%(message)s")


class TestRotateArray(unittest.TestCase):
    def test_rotate_array(self):
        self.assertEqual(rotate(nums=[1, 2, 3, 4, 5, 6, 7], k=3), [5, 6, 7, 1, 2, 3, 4])
        self.assertEqual(rotate(nums=[-1, -100, 3, 99], k=2), [3, 99, -1, -100])

    def test_rotate_group_array(self):
        self.assertEqual(
            rotate_group(nums=[1, 2, 3, 4, 5, 6, 7], k=3), [5, 6, 7, 1, 2, 3, 4]
        )
        self.assertEqual(rotate_group(nums=[-1, -100, 3, 99], k=2), [3, 99, -1, -100])
