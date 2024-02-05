"""
"""

import unittest

from leetcode_questions.common_word import most_common_word


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
