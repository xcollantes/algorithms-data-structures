"""Unit test for basic_calculator.py.

227. Basic Calculator II

Solved Medium Topics Companies Given a string s which represents an expression,
evaluate this expression and return its value.

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate
results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings
as mathematical expressions, such as eval().
"""

import unittest

from leetcode_questions.med.strings_arrays.basic_calculator import basic_calculator


class TestBasicCalculator(unittest.TestCase):
    def test_basic_calculator(self):
        self.assertEqual(basic_calculator("3+2*2"), 7)
        self.assertEqual(basic_calculator(" 3/2 "), 1)
        self.assertEqual(basic_calculator(" 3+5 / 2 "), 5)
