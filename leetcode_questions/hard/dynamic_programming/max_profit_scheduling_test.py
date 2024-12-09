"""Unit test for max_profit_scheduling.py.

1235. Maximum Profit in Job Scheduling

We have n jobs, where every job is scheduled to be done from start_time[i] to
end_time[i], obtaining a profit of profit[i].

You're given the start_time, end_time and profit arrays, return the maximum profit
you can take such that there are no two jobs in the subset with overlapping time
range.

If you choose a job that ends at time X you will be able to start another job
that starts at time X.

https://leetcode.com/problems/maximum-profit-in-job-scheduling/description
"""

import unittest

from leetcode_questions.hard.dynamic_programming.max_profit_scheduling import (
    job_scheduling,
)


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
            job_scheduling(start_time=[1, 1, 1], end_time=[2, 3, 4], profit=[5, 6, 4]),
            6,
        )
