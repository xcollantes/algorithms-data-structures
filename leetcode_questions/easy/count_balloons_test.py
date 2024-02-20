"""Unit test for count_balloons.py."""

import logging
import unittest

from leetcode_questions.count_balloons import count_balloons

logging.basicConfig(level=logging.INFO, format="%(message)s")


class TestBalloons(unittest.TestCase):
    def test_balloons(self):
        self.assertEqual(count_balloons("nlaebolko"), 1)
        self.assertEqual(count_balloons("loonbalxballpoon"), 2)
        self.assertEqual(count_balloons("leetcode"), 0)
        self.assertEqual(count_balloons("lloo"), 0)
