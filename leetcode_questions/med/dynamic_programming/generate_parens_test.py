"""Unit test for generate_parens.py.

22. Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of
well-formed parentheses.
"""

import unittest

from leetcode_questions.med.dynamic_programming.generate_parens import (
    generateParenthesis,
)


class TestGenerateParens(unittest.TestCase):
    def test_generate_parens(self):
        self.assertEqual(
            sorted(generateParenthesis(3)),
            sorted(["((()))", "(()())", "(())()", "()(())", "()()()"]),
        )
        self.assertEqual(generateParenthesis(1), ["()"])
