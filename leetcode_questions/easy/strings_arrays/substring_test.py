"""Unit test for substring.py."""

import unittest
import logging

from leetcode_questions.easy.strings_arrays.substring import is_subsequence

logging.basicConfig(level=logging.INFO, format="%(message)s")


class TestSubstring(unittest.TestCase):
    def test_substring(self):
        self.assertTrue(is_subsequence(s="abc", t="ahbgdc"))
        self.assertTrue(is_subsequence(s="", t="ahbgdc"))
        self.assertTrue(is_subsequence(s="u", t="u"))
        self.assertTrue(is_subsequence(s="aaaabbbb", t="aaaabvbbbbb"))

        self.assertFalse(is_subsequence(s="axc", t="ahbgdc"))
        self.assertFalse(is_subsequence(s="axc", t=""))
        self.assertFalse(is_subsequence(s="xxxxx", t="awopeirjspps"))
