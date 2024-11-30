"""819. Most Common Word

Given a string paragraph and a string array of the banned words banned, return
the most frequent word that is not banned. It is guaranteed there is at least
one word that is not banned, and that the answer is unique.

The words in paragraph are case-insensitive and the answer should be returned in
lowercase.
"""

import unittest

from leetcode_questions.easy.strings_arrays.common_word import most_common_word


class TestCommonWord(unittest.TestCase):
    def test_common(self):
        self.assertEqual(
            most_common_word(
                "..Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]
            ),
            "ball",
        )
        self.assertEqual(most_common_word("Bob. hIt, baLl", ["bob", "hit"]), "ball")
        self.assertEqual(
            most_common_word(
                "abc abc? abcd the jeff!",
                ["abc", "abcd", "jeff"],
            ),
            "the",
        )
