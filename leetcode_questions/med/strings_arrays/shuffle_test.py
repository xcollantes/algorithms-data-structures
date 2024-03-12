"""Unit test for shuffle.py."""

import unittest
import logging

from leetcode_questions.med.strings_arrays.shuffle import Shuffle

logging.basicConfig(level=logging.INFO, format="%(message)s")


class TestShuffle(unittest.TestCase):
    def test_shuffle(self):
        a = [1, 2, 3]
        s = Shuffle(a)

        prev = []
        x = s.shuffle()
        prev.append(x)
        self.assertNotEqual(x, a)

        self.assertEqual(s.reset(), a)

        i = s.shuffle()
        prev.append(i)
        self.assertNotIn(a, prev)
