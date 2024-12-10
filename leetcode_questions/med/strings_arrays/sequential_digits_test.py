"""Unit test for sequential_digits.py.

1291. Sequential Digits

An integer has sequential digits if and only if each digit in the number is one
more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that
have sequential digits.

Constraints:
10 <= low <= high <= 10^9
"""

import unittest

from leetcode_questions.med.strings_arrays.sequential_digits import (
    LeetcodeSolution,
    SamSolution,
    XavierSolution,
)


class TestSequentialDigits(unittest.TestCase):
    def test_leetcode(self):
        self.cases(LeetcodeSolution().sequentialDigits)

    def test_xavier(self):
        """Works algorithmically but will timeout in Leetcode."""
        self.cases(XavierSolution().sequentialDigits)

    def test_sam(self):
        self.cases(SamSolution().sequentialDigits)

    def cases(self, fn):
        self.assertEqual(fn(100, 300), [123, 234])
        self.assertEqual(fn(1000, 13000), [1234, 2345, 3456, 4567, 5678, 6789, 12345])
        self.assertEqual(
            fn(10, 100000000),
            [
                12,
                23,
                34,
                45,
                56,
                67,
                78,
                89,
                123,
                234,
                345,
                456,
                567,
                678,
                789,
                1234,
                2345,
                3456,
                4567,
                5678,
                6789,
                12345,
                23456,
                34567,
                45678,
                56789,
                123456,
                234567,
                345678,
                456789,
                1234567,
                2345678,
                3456789,
                12345678,
                23456789,
            ],
        )
