"""Unit test for make_string_great.py."""

import unittest
import logging

from leetcode_questions.easy.stacks_queues.make_string_great import make_great

logging.basicConfig(level=logging.INFO, format="%(message)s")


class TestMakeStringGreat(unittest.TestCase):
    def test_make_string_great(self):
        self.assertEqual(make_great("leEeetcode"), "leetcode")
        self.assertEqual(make_great("abBAcC"), "")
        self.assertEqual(make_great("s"), "s")
