"""Unit test for parens.py."""

import unittest
import logging

from leetcode_questions.med.parens import valid_parens

logging.basicConfig(level=logging.INFO, format="%(message)s")


class TestParens(unittest.TestCase):
    def test_parens(self):
        self.assertEqual(valid_parens("()"), True)
        self.assertEqual(valid_parens("()[]{}"), True)
        self.assertEqual(valid_parens("(]"), False)
        self.assertEqual(valid_parens("]"), False)
        self.assertEqual(valid_parens("[[}}}]]"), False)
