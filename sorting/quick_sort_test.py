"""Unittest for quick_sort.py"""

import unittest
import logging
from sorting.quick_sort import quicksort

logging.basicConfig(level=logging.INFO, format="%(message)s")


class TestQuickSort(unittest.TestCase):
    def test_recursive(self):
        test_arrays = [
            [39, 19, 38, 88, 134, 32, 28, 142, 56, 67],
            [1],
            [],
            [1, 2, 2, 3],
        ]

        for test in test_arrays:
            expected = sorted(test.copy())
            logging.info(expected)

            l: int = len(test)
            result = quicksort(test, 0, l - 1)

            logging.info(f"RESULT: {result}")

            self.assertEqual(
                result,
                expected,
            )
