"""Unit test for log_files.py."""

import unittest

from leetcode_questions.log_files import reorder_optimal


class TestLogs(unittest.TestCase):
    # def test_logs(self):
    #     self.assertEqual(
    #         reorder_logs(
    #             [
    #                 "dig1 8 1 5 1",
    #                 "let1 art can",
    #                 "dig2 3 6",
    #                 "let2 own kit dig",
    #                 "let3 art zero",
    #             ]
    #         ),
    #         [
    #             "let1 art can",
    #             "let3 art zero",
    #             "let2 own kit dig",
    #             "dig1 8 1 5 1",
    #             "dig2 3 6",
    #         ],
    #     )

    def test_optimized(self):
        self.assertEqual(
            reorder_optimal(
                [
                    "dig1 8 1 5 1",
                    "let1 art can",
                    "dig2 3 6",
                    "let2 own kit dig",
                    "let3 art zero",
                ]
            ),
            [
                "let1 art can",
                "let3 art zero",
                "let2 own kit dig",
                "dig1 8 1 5 1",
                "dig2 3 6",
            ],
        )
