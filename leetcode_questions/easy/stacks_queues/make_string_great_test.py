"""Unit test for make_string_great.py.

Given a string s of lower and upper case English letters.

A good string is a string which doesn't have two adjacent characters s[i] and
s[i + 1] where:

0 <= i <= s.length - 2 s[i] is a lower-case letter and s[i + 1] is the same
letter but in upper-case or vice-versa.  To make the string good, you can choose
two adjacent characters that make the string bad and remove them. You can keep
doing this until the string becomes good.

Return the string after making it good. The answer is guaranteed to be unique
under the given constraints.

Notice that an empty string is also good.
"""

import unittest
import logging

from leetcode_questions.easy.stacks_queues.make_string_great import make_great

logging.basicConfig(level=logging.INFO, format="%(message)s")


class TestMakeStringGreat(unittest.TestCase):
    def test_make_string_great(self):
        self.assertEqual(make_great("leEeetcode"), "leetcode")
        self.assertEqual(make_great("abBAcC"), "")
        self.assertEqual(make_great("s"), "s")
