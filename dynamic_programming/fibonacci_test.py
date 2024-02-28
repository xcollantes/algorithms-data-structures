"""Unit test for fibonacci.py."""

import unittest
import logging

from dynamic_programming.fibonacci import fibo

logging.basicConfig(level=logging.INFO, format="%(message)s")


class TestFibonacci(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(fibo(1), 1)
        self.assertEqual(fibo(0), 0)
        self.assertEqual(fibo(20), 6765)
