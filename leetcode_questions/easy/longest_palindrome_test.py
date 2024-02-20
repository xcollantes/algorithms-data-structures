"""Unit test for longest_palindrome.py."""

import unittest

from leetcode_questions.longest_palindrome import is_palindrome, palindrome


class TestLongestPalindrome(unittest.TestCase):
    def test_palindrome(self):
        self.assertEqual(palindrome("babad"), "bab")
        self.assertEqual(palindrome("cbbd"), "bb")

    def test_palindrome_helper(self):
        self.assertEqual(is_palindrome("hello"), False)
        self.assertEqual(is_palindrome("aba"), True)
        self.assertEqual(is_palindrome("bbbbb"), True)
        self.assertEqual(is_palindrome("a"), True)
        self.assertEqual(is_palindrome("ab"), False)
