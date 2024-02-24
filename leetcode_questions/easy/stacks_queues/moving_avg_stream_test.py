"""Unit test for moving_avg_stream.py."""

import unittest
import logging

from leetcode_questions.easy.stacks_queues.moving_avg_stream import MovingAvg


logging.basicConfig(level=logging.INFO, format="%(message)s")


class TestMovingAvgStream(unittest.TestCase):
    def test_moving_avg_stream(self):
        moving_avg = MovingAvg(3)

        self.assertEqual(moving_avg.next(1), 1.0)
        self.assertEqual(moving_avg.next(10), 5.5)
        self.assertAlmostEqual(moving_avg.next(3), 4.66667, places=2)
        self.assertEqual(moving_avg.next(5), 6.0)
