"""Unit test for count_and_say.py."""

import logging
import unittest

from leetcode_questions.med.strings_arrays.count_and_say import countAndSay, countAndSayIterative

logging.basicConfig(level=logging.INFO, format="%(message)s")


class TestCountAndSay(unittest.TestCase):
    def test_count_and_say(self):
        self.cases(countAndSay)

    def test_iterative(self):
        self.cases(countAndSayIterative)

    def cases(self, fn):
        # Explanation:
        #     countAndSay(1) = "1"
        #     countAndSay(2) = RLE of "1" = "11"
        #     countAndSay(3) = RLE of "11" = "21"
        #     countAndSay(4) = RLE of "21" = "1211"
        self.assertEqual(fn(4), "1211")

        # Explanation:
        # This is the base case.
        self.assertEqual(fn(1), "1")
