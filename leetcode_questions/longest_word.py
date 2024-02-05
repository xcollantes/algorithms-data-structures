"""
Given a string s, find the length of the longest substring without repeating
characters.

"""

import logging

logging.basicConfig(level=logging.INFO)


def length_of_longest_substring(s: str) -> int:
    chars = set()
    max_length = 0
    left = 0

    for right in range(len(s)):
        if s[right] in chars:
            while s[right] in chars:
                chars.remove(s[left])
                left += 1

            chars.add(s[right])
        else:
            chars.add(s[left])
            max_length = max(max_length, right - left + 1)

    return max_length
