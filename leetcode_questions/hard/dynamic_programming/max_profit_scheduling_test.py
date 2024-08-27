"""Unit test for max_profit_scheduling.py."""

import unittest
import logging

from leetcode_questions.hard.dynamic_programming.max_profit_scheduling import job_scheduling

logging.basicConfig(level=logging.INFO, format="%(message)s")


class TestMaxProfitScheduling(unittest.TestCase):
    def test_max_profit_scheduling(self):
        self.assertEqual(
            job_scheduling(
                start_time=[1, 2, 3, 3], end_time=[3, 4, 5, 6], profit=[50, 10, 40, 70]
            ),
            120,
        )
        self.assertEqual(
            job_scheduling(
                start_time=[1, 2, 3, 4, 6],
                end_time=[3, 5, 10, 6, 9],
                profit=[20, 20, 100, 70, 60],
            ),
            150,
        )
        self.assertEqual(
            job_scheduling(start_time=[1, 1, 1], end_time=[2, 3, 4], profit=[5, 6, 4]), 6
        )