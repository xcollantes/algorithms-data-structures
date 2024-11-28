"""Unit test for shuffle.py."""

import unittest

from leetcode_questions.med.strings_arrays.shuffle import Shuffle


class TestShuffle(unittest.TestCase):
    def test_shuffle(self):
        prev = []
        a = [1, 2, 3]
        ORIGINAL = a[:]
        s = Shuffle(a)

        first = s.shuffle()
        prev.append(tuple(first))
        print(s.nums)
        self.assertNotIn(first, prev)

        self.assertEqual(s.reset(), ORIGINAL)
        print(s.nums)

        second = s.shuffle()
        print(s.nums)
        prev.append(tuple(second))
        self.assertNotIn(second, prev)
