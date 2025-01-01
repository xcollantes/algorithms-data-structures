"""1249. Minimum Remove to Make Valid Parentheses

Medium

Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any
positions ) so that the resulting parentheses string is valid and return any
valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.


Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.


Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"


Example 3:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.


Constraints:

1 <= s.length <= 105
s[i] is either '(' , ')', or lowercase English letter.
"""

import unittest

from leetcode_questions.med.stacks_queues.min_parens import min_parens


class TestMinParens(unittest.TestCase):

    def test_min_parens(self):
        cases = [
            ("lee(t(c)o)de)", "lee(t(c)o)de"),
            ("a)b(c)d", "ab(c)d"),
            ("))((", ""),
        ]

        for s, output in cases:
            with self.subTest(s=s, output=output):
                print(f"{s} expected: {output}")
                self.assertEqual(min_parens(s), output)
