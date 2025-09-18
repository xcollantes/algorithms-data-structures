"""459. Repeated Substring Pattern

Easy

Given a string s, check if it can be constructed by taking a substring of it and
appending multiple copies of the substring together.


Example 1:

Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.


Example 2:

Input: s = "aba"
Output: false
Example 3:

Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or the substring "abcabc" twice.


Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.
"""


def test_repeat_substring():
    """pytest repeat_substring.py"""
    assert repeat_substring("abab") == True
    assert repeat_substring("aba") == False
    assert repeat_substring("abcabcabcabc") == True


def repeat_substring(s: str) -> bool:
    """
    Solution is O(n) time.

    Optimal way is to check for the overlapping pattern of the string and check
    if the original string is in the overlapping pattern.

    The first and last character are removed because they would be the redundant
    characters in the overlapping pattern.
    """

    print(f"s {s}")

    combined = s + s

    print(f"(s + s) {combined}")
    print(f"index: {combined[1 : -1]}")

    return s in combined[1:-1]
