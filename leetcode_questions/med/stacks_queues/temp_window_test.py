"""Unit test for temp_window.py."""

import unittest
import logging

from leetcode_questions.med.stacks_queues.temp_window import daily_temps

logging.basicConfig(level=logging.INFO, format="%(message)s")


class TestTempWindow(unittest.TestCase):
    def test_temp_window(self):
        self.assertEqual(
            daily_temps([73, 74, 75, 71, 69, 72, 76, 73]), [1, 1, 4, 2, 1, 1, 0, 0]
        )
        self.assertEqual(daily_temps([30, 40, 50, 60]), [1, 1, 1, 0])
        self.assertEqual(daily_temps([30, 60, 90]), [1, 1, 0])
