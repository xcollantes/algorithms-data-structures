"""Unit test for number_of_islands.py."""

import unittest

from leetcode_questions.number_of_islands import islands


class TestIslands(unittest.TestCase):
    def test_islands(self):
        self.assertEquals(
            islands(
                [
                    ["1", "1", "1", "1", "0"],
                    ["1", "1", "0", "1", "0"],
                    ["1", "1", "0", "0", "0"],
                    ["0", "0", "0", "0", "0"],
                ]
            ),
            1,
        )

        self.assertEquals(
            islands(
                [
                    ["1", "1", "0", "0", "0"],
                    ["1", "1", "0", "0", "0"],
                    ["0", "0", "1", "0", "0"],
                    ["0", "0", "0", "1", "1"],
                ]
            ),
            3,
        )
