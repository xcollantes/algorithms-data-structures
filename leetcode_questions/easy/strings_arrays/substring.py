"""392. Is Subsequence

Given two strings s and t, return true if s is a subsequence of t, or false
otherwise.

A subsequence of a string is a new string that is formed from the original
string by deleting some (can be none) of the characters without disturbing the
relative positions of the remaining characters. (i.e., "ace" is a subsequence of
"abcde" while "aec" is not).

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
"""


def is_subsequence(s: str, t: str) -> bool:
    """Faster and more efficient method."""
    if len(s) <= 0:
        return True

    s_ptr: int = 0
    for letter in t:
        if s[s_ptr] == letter:
            s_ptr += 1

        if s_ptr == len(s):
            return True

    return False


def is_subsequence_alt(s: str, t: str) -> bool:
    s_ptr = 0
    t_ptr = 0

    while s_ptr < len(s) and t_ptr < len(t):
        if s[s_ptr] == t[t_ptr]:
            s_ptr += 1
        t_ptr += 1

    return s_ptr == len(s)
