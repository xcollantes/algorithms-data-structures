"""76. Minimum Window Substring

Hard

Given two strings s and t of lengths m and n respectively, return the minimum
window substring of s such that every character in t (including duplicates) is
included in the window. If there is no such substring, return the empty string
"".

The testcases will be generated such that the answer is unique.


Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.


Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.


Follow up: Could you find an algorithm that runs in O(m + n) time?
"""

from collections import defaultdict


def test_min_substring():
    """pytest min_substring.py"""
    assert min_substring("ADOBECODEBANC", "ABC") == "BANC"
    # assert min_substring("a", "a") == "a"
    # assert min_substring("a", "aa") == ""
    # assert min_substring("ab", "a") == "a"
    # assert min_substring("ab", "b") == "b"


def min_substring(s: str, target: str) -> str:
    """"""

    if len(s) < len(target):
        return ""

    # get count dict so we decrease as we find new chars.
    # chars we care about will be 0 if found; chars we don't care about will be
    # < 0.
    ch_counts = defaultdict(int)
    for c in target:
        ch_counts[c] += 1

    req = len(target)

    min_window = (0, len(s) + 1)
    start = 0

    # iterate left to right
    for end in range(len(s)):
        print(s)
        print(f"{' ' * start}x")
        print(f"{' ' * (end - 1)}y")
        print(f"start {start} end {end} {ch_counts}")

        if ch_counts[s[end]] > 0:
            print(f"found {s[end]}")
            req -= 1

        # chars we don't care about will be < 0.
        ch_counts[s[end]] -= 1

        # shrink when all target letters found.
        if req == 0:
            # shrink left to right.
            # if required letter is removed, break.
            # we can tell char is required because required chars are 0 at this
            # point.
            while ch_counts[s[start]] != 0:
                ch_counts[s[start]] += 1  # This is undoing the subtraction above.
                start += 1

            # get new smaller window.
            if end - start < min_window[1] - min_window[0]:
                min_window = (start, end)

            ch_counts[s[start]] += 1
            start += 1
            req += 1

    print(f"result min_window: {min_window}")

    # check if length of min_window changed; return "" if unchanged.
    if min_window[1] > len(s):
        return ""
    return s[min_window[0] : min_window[1] + 1]


from leetcode_questions.utils.models.leetcode_data_models import (
    Difficulty,
    Metadata,
    Tags,
)

__metadata__ = Metadata(
    tags=[Tags.HASH_TABLE, Tags.STRING, Tags.SLIDING_WINDOW],
    difficulty=Difficulty.HARD,
)
