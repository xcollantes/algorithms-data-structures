"""791. Custom Sort String

Medium

You are given two strings order and s. All the characters of order are unique
and were sorted in some custom order previously.

Permute the characters of s so that they match the order that order was sorted.
More specifically, if a character x occurs before a character y in order, then x
should occur before y in the permuted string.

Return any permutation of s that satisfies this property.
"""

import unittest

from leetcode_questions.med.strings_arrays.custom_sort import custom_sort


class TestCustomSort(unittest.TestCase):
    def test_custom_sort(self):

        # Since "d" does not appear in order, it can be at any position in the
        # returned string. "dcba", "cdba", "cbda" are also valid outputs.
        a = custom_sort("cba", "abcd")
        print(f"A: {a}")
        self.assertIn(
            a.replace("d", ""), ["cba", "cba", "cba", "cba"]
        )

        b = custom_sort("bcafg", "abcd")
        print(f"B: {b}")
        self.assertIn(
            b.replace("d", ""), ["bca", "dca", "bca"]
        )
