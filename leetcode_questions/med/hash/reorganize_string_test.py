"""Unit test for reorganize_string.py.

767. Reorganize String

Given a string s, rearrange the characters of s so that any two adjacent
characters are not the same.

Return any possible rearrangement of s or return "" if not possible.

https://leetcode.com/problems/reorganize-string/description
"""

import unittest


class TestReorganizeString(unittest.TestCase):
    def test_reorganize_string(self):
        self.assertEqual(reorganize_string(s="aab"), "aba")
        self.assertEqual(reorganize_string(s="aaab"), "")
        self.assertEqual(reorganize_string(s="aaabbccc"), "acacabcb")
        self.assertEqual(reorganize_string(s="aaaaaabc"), "")
