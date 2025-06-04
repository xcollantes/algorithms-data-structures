"""
Given a string s, find the length of the longest substring without repeating
characters.

"""


def test_length_of_longest_substring():
    """pytest longest_word.py"""
    assert length_of_longest_substring("abcabcbb") == 3  # "abc"
    assert length_of_longest_substring("pwwke") == 3  # "wke"
    assert length_of_longest_substring("bbbbbbbbb") == 1  # "b"
    assert length_of_longest_substring("dvdf") == 3  # "dvdf"


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


from leetcode_questions.utils.models.leetcode_data_models import (
    Difficulty,
    Metadata,
    Tags,
)

__metadata__ = Metadata(
    tags=[Tags.ARRAY, Tags.STRING, Tags.SORTING],
    difficulty=Difficulty.EASY,
)
