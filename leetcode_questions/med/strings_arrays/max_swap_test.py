"""670. Maximum Swap

Medium

You are given an integer num. You can swap two digits at most once to get the
maximum valued number.

Return the maximum valued number you can get.


Example 1:

Input: num = 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.


Example 2:

Input: num = 9973
Output: 9973
Explanation: No swap.


Constraints: 0 <= num <= 108
"""

import unittest

from leetcode_questions.med.strings_arrays.max_swap import max_swap


class TestMaxSwap(unittest.TestCase):
    def test_max_swap(self):
        self.assertEqual(max_swap(2736), 7236)
        self.assertEqual(max_swap(27836), 87236)
        self.assertEqual(max_swap(9973), 9973)
