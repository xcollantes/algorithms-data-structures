"""408. Valid Word Abbreviation

Easy

A string can be abbreviated by replacing any number of non-adjacent, non-empty
substrings with their lengths. The lengths should not have leading zeros.

For example, a string such as "substitution" could be abbreviated as (but not
limited to):

"s10n" ("s ubstitutio n")
"sub4u4" ("sub stit u tion")
"12" ("substitution")
"su3i1u2on" ("su bst i t u ti on")
"substitution" (no substrings replaced)
The following are not valid abbreviations:

"s55n" ("s ubsti tutio n", the replaced substrings are adjacent)
"s010n" (has leading zeros)
"s0ubstitution" (replaces an empty substring)
Given a string word and an abbreviation abbr, return whether the string matches the given abbreviation.

A substring is a contiguous non-empty sequence of characters within a string.

Example 1:

Input: word = "internationalization", abbr = "i12iz4n"
Output: true
Explanation: The word "internationalization" can be abbreviated as "i12iz4n" ("i nternational iz atio n").

Example 2:

Input: word = "apple", abbr = "a2e"
Output: false
Explanation: The word "apple" cannot be abbreviated as "a2e".

Constraints:

1 <= word.length <= 20
word consists of only lowercase English letters.
1 <= abbr.length <= 10
abbr consists of lowercase English letters and digits.
All the integers in abbr will fit in a 32-bit integer.
"""


def test_word_abbr():
    """pytest word_abbr.py"""
    assert word_abbr("internationalization", "i12iz4n") == True
    assert word_abbr("apple", "a2e") == False
    assert word_abbr("a", "2") == False
    assert word_abbr("internationalization", "i5a11o1") == True
    assert word_abbr("hi", "2i") == False


def word_abbr(word: str, abbr: str) -> bool:
    """
    "internationalization", abbr = "i5a11o1"
               w
                                          a
    """
    w = 0
    a = 0

    while w < len(word) and a < len(abbr):

        if w >= len(word) or abbr[a] == "0":
            return False

        num = ""

        while a < len(abbr) and abbr[a].isdigit():
            num += abbr[a]
            a += 1

        if num:
            w += int(num)
        else:
            if word[w] != abbr[a]:
                return False

            w += 1
            a += 1

    return w == len(word) and a == len(abbr)


from leetcode_questions.utils.models.leetcode_data_models import (
    Difficulty,
    Metadata,
    Tags,
)

__metadata__ = Metadata(
    tags=[Tags.STRING, Tags.TWO_POINTERS],
    difficulty=Difficulty.EASY,
)
