"""Unit test for string_eval.py."""

import unittest
import logging

from leetcode_questions.med.strings_arrays.string_eval import string_eval

logging.basicConfig(level=logging.INFO, format="%(message)s")


class TestStringEval(unittest.TestCase):
    def test_string_eval(self):
        self.assertEqual(string_eval(s="3+2*2"), 7)
        self.assertEqual(string_eval(s=" 3/2 "), 1)
        self.assertEqual(string_eval(s=" 3+5 / 2 "), 5)
        self.assertEqual(string_eval(s="14-3/2"), 12)
