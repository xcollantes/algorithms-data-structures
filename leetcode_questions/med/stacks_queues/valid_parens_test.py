"""20. Valid Parentheses

Easy

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.  Open brackets must
be closed in the correct order.  Every close bracket has a corresponding open
bracket of the same type.

Example 1: Input: s = "()" Output: true

Example 2: Input: s = "()[]{}" Output: true

Example 3: Input: s = "(]" Output: false

Example 4: Input: s = "([])" Output: true
"""

import unittest

from leetcode_questions.med.stacks_queues.valid_parens import is_valid


class TestValidParens(unittest.TestCase):
    def test_parens(self):
        self.assertTrue(is_valid("()"))
        self.assertTrue(is_valid("()[]{}"))
        self.assertTrue(is_valid("([])"))
        self.assertFalse(is_valid("(]"))
        self.assertFalse(is_valid("]"))
        self.assertFalse(is_valid("[[}}}]]"))
