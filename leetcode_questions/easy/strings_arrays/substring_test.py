"""Unit test for substring.py.

392. Is Subsequence

Given two strings s and t, return true if s is a subsequence of t, or false
otherwise.

A subsequence of a string is a new string that is formed from the original
string by deleting some (can be none) of the characters without disturbing the
relative positions of the remaining characters. (i.e., "ace" is a subsequence of
"abcde" while "aec" is not).

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
"""

import unittest
from leetcode_questions.easy.strings_arrays.substring import is_subsequence


class TestSubstring(unittest.TestCase):
    def test_substring(self):
        self.assertTrue(is_subsequence(s="abc", t="ahbgdc"))
        self.assertTrue(is_subsequence(s="", t="ahbgdc"))
        self.assertTrue(is_subsequence(s="u", t="u"))
        self.assertTrue(is_subsequence(s="aaaabbbb", t="aaaabvbbbbb"))

        self.assertFalse(is_subsequence(s="axc", t="ahbgdc"))
        self.assertFalse(is_subsequence(s="axc", t=""))
        self.assertFalse(is_subsequence(s="xxxxx", t="awopeirjspps"))
