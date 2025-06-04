"""14. Longest Common Prefix

Easy

Write a function to find the longest common prefix string amongst an array of
strings.

If there is no common prefix, return an empty string "".


Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"


Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.
"""


def test_min_prefix():
    """pytest min_prefix.py"""
    assert min_prefix(["flower", "flight", "flow"]) == "fl"
    assert min_prefix(["dog", "racecar", "car"]) == ""
    assert min_prefix(["flower", "flare", "flow", "flight", "flew"]) == "fl"


def min_prefix(strs: list[str]) -> str:
    """
    flower == flare
      i
               x
    fl == flow
     i
           x

    fl == fot
    i
          x
    """
    compare = strs[0]
    i = len(compare)

    for word in strs[1:]:

        print(f"{compare} {i} {word} compare {compare[:i]}")

        # move pointer from right to left until matches.
        # from there, match other words.
        while compare[:i] != word[:i]:
            i -= 1

        # found match.
        compare = compare[:i]

    return compare


from leetcode_questions.utils.models.leetcode_data_models import (
    Difficulty,
    Metadata,
    Tags,
)

__metadata__ = Metadata(
    tags=[Tags.STRING, Tags.TRIE],
    difficulty=Difficulty.EASY,
)
