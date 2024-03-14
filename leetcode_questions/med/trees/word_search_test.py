"""Unit test for word_search.py."""

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
