"""Unit test for insertion_sort.py."""

import unittest
from sorting import insertion_sort


class TestInsertionSort(unittest.TestCase):
    def test_insertion_sort(self):
        """Test insertion_sort.py."""
        self.cases(insertion_sort.insertion)

    def cases(self, fn):
        self.assertEqual(
            fn([39, 19, 38, 88, 134, 32, 28, 142, 56, 67]),
            [
                19,
                28,
                32,
                38,
                39,
                56,
                67,
                88,
                134,
                142,
            ],
        )
        self.assertEqual(fn([1]), [1])
        self.assertEqual(fn([]), [])
        self.assertEqual(fn([1, 2, 2, 3]), [1, 2, 2, 3])
