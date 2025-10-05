"""139. Word Break

Medium

Given a string s and a dictionary of strings word_dict, return true if s can be
segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the
segmentation.


Example 1:

Input: s = "leetcode", word_dict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".


Example 2:

Input: s = "applepenapple", word_dict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.


Example 3:

Input: s = "catsandog", word_dict = ["cats","dog","sand","and","cat"]
Output: false


Constraints:

1 <= s.length <= 300
1 <= word_dict.length <= 1000
1 <= word_dict[i].length <= 20
s and word_dict[i] consist of only lowercase English letters.
All the strings of word_dict are unique.
"""


def test_word_break_simple():
    """pytest word_break.py"""
    assert word_break(s="leetcode", word_list=["leet", "code"]) == True


def test_word_break():
    """pytest word_break.py"""
    assert word_break(s="applepenapple", word_list=["apple", "pen"]) == True
    assert (
        word_break(s="catsandog", word_list=["cats", "dog", "sand", "and", "cat"])
        == False
    )


from collections import deque


def word_break(s: str, word_list: list[str]) -> bool:

    visited = set()

    queue = deque([0])

    while queue:
        start = queue.popleft()

        if start not in visited:

            for end in range(start + 1, len(s) + 1):
                if s[start:end] in word_list:
                    queue.append(end)

                    if end == len(s):
                        return True

            visited.add(start)

    return False
