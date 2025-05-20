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
    print(f"s {s} t {target}")

    # check if valid
    if len(s) < len(target):
        return ""

    # Track the count of each character in the target string.
    ch_count = defaultdict(int)
    for ch in target:
        ch_count[ch] += 1

    print(f"count ch in t for easy tracking: ch_count: {ch_count}")

    # Needed since we want to find the min window size.
    # Starting with infinitely, any window we find will be smaller.
    #
    target_ch_remain = len(target)
    min_window = (0, float("inf"))
    print(f"min window: {min_window}")
    start_i = 0

    for end_i in range(len(s)):
        print(s)
        print(f"{' ' * (start_i)}x")
        print(f"{' ' * (end_i)}y")

        # print(f"check if cur ch still looking for: {s[end_i]}")
        if ch_count[s[end_i]] > 0:
            print(f"found {s[end_i]}")

            target_ch_remain -= 1

        ch_count[s[end_i]] -= 1
        print(f"target str remaining: {target_ch_remain} {ch_count}")

        # Shrink window.
        if target_ch_remain == 0:
            print(f"no target chars remaining: {target_ch_remain}")

            # Start from left side to shrink current window.
            while True:
                print(f"shrink from left side until invalid: {s[start_i: end_i]} {start_i} {end_i}")
                print(f"ch_count: {ch_count}")

                char_at_start = s[start_i]

                # If ch_count is disrupted, then we can't remove.
                # Zero is the required counts and non-required is less than
                # zero.
                if ch_count[char_at_start] == 0:
                    break

                ch_count[char_at_start] += 1
                start_i += 1  # Move left ptr right-ward.

            print(f"found break: {start_i} {end_i}")

            print(f"min: {min_window}")
            # Update min window.
            # If the current positions of end and start are smaller than the
            # currently stored end and start, then replace.
            if end_i - start_i < min_window[1] - min_window[0]:
                min_window = (start_i, end_i)

            # Prepare for next window.
            ch_count[s[start_i]] += 1
            target_ch_remain += 1
            start_i += 1

        print()

    print(f"end min: {min_window}")

    # If no valid window found, check if min_window is still at infinity.
    return "" if min_window[1] > len(s) else s[min_window[0] : min_window[1] + 1]
