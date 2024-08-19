"""Unit test for remove_element.py."""

import unittest
import logging

from leetcode_questions.easy.strings_arrays.remove_element import remove_element

logging.basicConfig(level=logging.INFO, format="%(message)s")


class TestRemoveElement(unittest.TestCase):
    def test_remove_element(self):
        self.assertEqual(remove_element(nums=[3, 2, 2, 3], val=3), 2)
        self.assertEqual(remove_element(nums=[0, 1, 2, 2, 3, 0, 4, 2], val=2), 5)
