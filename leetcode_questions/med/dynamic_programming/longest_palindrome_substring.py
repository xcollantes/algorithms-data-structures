"""5. Longest Palindromic Substring

Medium

Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:

Input: s = "cbbd"
Output: "bb"

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""


def test_longest_palindrome_substring():
    """pytest longest_palindrome_substring.py"""
    assert longest_palindrome_substring("babad") == "bab"
    assert longest_palindrome_substring("cbbd") == "bb"


def longest_palindrome_substring(s: str) -> str:
    """"""
    return 0


from leetcode_questions.utils.models.leetcode_data_models import (
    Difficulty,
    Metadata,
    Tags,
)

__metadata__ = Metadata(
    tags=[Tags.DYNAMIC_PROGRAMMING, Tags.STRING, Tags.PALINDROME],
    difficulty=Difficulty.MEDIUM,
)
