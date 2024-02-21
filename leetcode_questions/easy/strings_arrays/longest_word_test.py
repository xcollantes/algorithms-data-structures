"""Unit test for longest_word.py."""

import unittest

from leetcode_questions.longest_word import length_of_longest_substring


class TestLongestWord(unittest.TestCase):
    def test_words(self):
        self.assertEqual(length_of_longest_substring("abcabcbb"), 3)  # "abc"
        self.assertEqual(length_of_longest_substring("pwwke"), 3)  # "wke"
        self.assertEqual(length_of_longest_substring("bbbbbbbbb"), 1)  # "b"
        self.assertEqual(length_of_longest_substring("dvdf"), 3)  # "dvdf"
