"""Unit test for reorganize_string.py."""

import unittest
import logging

from leetcode_questions.med.hash.reorganize_string import reorganize_string

logging.basicConfig(level=logging.INFO, format="%(message)s")


class TestReorganizeString(unittest.TestCase):
    def test_reorganize_string(self):
        self.assertEqual(reorganize_string(s="aab"), "aba")
        self.assertEqual(reorganize_string(s="aaab"), "")
        self.assertEqual(reorganize_string(s="aaabbccc"), "acacabcb")
        self.assertEqual(reorganize_string(s="aaaaaabc"), "")
