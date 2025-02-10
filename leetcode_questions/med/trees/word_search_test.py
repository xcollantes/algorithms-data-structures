"""Unit test for word_search.py.

79. Word Search

Given an m x n grid of characters board and a string word, return true if word
exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where
adjacent cells are horizontally or vertically neighboring. The same letter cell
may not be used more than once.
"""

import unittest
import logging

from leetcode_questions.med.trees.word_search import WordSearch

logging.basicConfig(level=logging.INFO, format="%(message)s")


class TestWordSearch(unittest.TestCase):
    def test_word_search(self):
        w = WordSearch(
            board=[
                ["A", "B", "C", "E"],
                ["S", "F", "C", "S"],
                ["A", "D", "E", "E"],
            ],
        )

        self.assertTrue(
            w.word_search(
                word="ABCCED",
            ),
        )

        x = WordSearch(
            board=[
                ["A", "B", "C", "E"],
                ["S", "F", "C", "S"],
                ["A", "D", "E", "E"],
            ],
        )
        self.assertTrue(
            x.word_search(
                word="SEE",
            ),
        )

        y = WordSearch(
            board=[
                ["A", "B", "C", "E"],
                ["S", "F", "C", "S"],
                ["A", "D", "E", "E"],
            ],
        )
        self.assertFalse(
            y.word_search(
                word="ABCB",
            ),
        )
        z = WordSearch(
            board=[
                [
                    ["A", "A", "A", "A", "A", "A"],
                    ["A", "A", "A", "A", "A", "A"],
                    ["A", "A", "A", "A", "A", "A"],
                    ["A", "A", "A", "A", "A", "A"],
                    ["A", "A", "A", "A", "A", "A"],
                    ["A", "A", "A", "A", "A", "A"],
                ]
            ],
        )

        self.assertFalse(
            z.word_search(
                word="AAAAAAAAAAAAAAB",
            ),
        )
