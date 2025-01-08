"""680. Valid Palindrome II

Easy

Given a string s, return true if the s can be palindrome after deleting at most
one character from it.


Example 1:

Input: s = "aba"
Output: true


Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.


Example 3:

Input: s = "abc"
Output: false


Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
"""

import unittest

from leetcode_questions.easy.strings_arrays.palindrome_remove import valid_palindrome


class TestPalindromeRemove(unittest.TestCase):
    def test_palindrome_remove(self):
        self.assertEqual(valid_palindrome("aba"), True)
        print()
        self.assertEqual(valid_palindrome("abca"), True)
        print()
        self.assertEqual(valid_palindrome("abc"), False)
        print()
        self.assertEqual(valid_palindrome("abcdefedgcba"), True)
        print()
