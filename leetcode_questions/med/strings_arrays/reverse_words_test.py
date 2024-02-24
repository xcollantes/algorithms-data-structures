"""Unit test for reverse_words.py."""

import unittest
import logging

from leetcode_questions.med.strings_arrays.reverse_words import reverse_words

logging.basicConfig(level=logging.INFO, format="%(message)s")


class TestReverseWords(unittest.TestCase):
    def test_reverse_words(self):
        self.assertEqual(reverse_words("the sky is blue"), "blue is sky the")
        self.assertEqual(reverse_words("  hello world  "), "world hello")
        self.assertEqual(reverse_words("a good   example"), "example good a")
