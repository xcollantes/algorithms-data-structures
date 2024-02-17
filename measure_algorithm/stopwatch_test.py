"""Test for stopwatch.py."""

import unittest
import inspect
from stopwatch import Stopwatch


class TestStopwatch(unittest.TestCase):
    def _bubble_sort(self, input: list):
        """Simple sorting for test."""
        if len(input) < 1:
            return input
        idx: int = 0
        for _ in range(len(input)):
            while idx < len(input) - 1:
                if input[idx] > input[idx + 1]:
                    input[idx], input[idx + 1] = input[idx + 1], input[idx]
                idx += 1
            idx = 0
        return input

    def test_stopwatch(self):
        test_list: list = [3, 4, 1, 56, 1, 2, 12, 0]
        f = inspect.getsource(self._bubble_sort)
        f += f"\n{self._bubble_sort.__name__.strip()}()"
        print(f)

        print(inspect.cleandoc(self._bubble_sort))

        s = Stopwatch(function_to_measure=self._bubble_sort)

        s.run()
        s.print_results()
        self.assertTrue(True)
