"""Unit test for fibonacci.py."""

import unittest
import logging

from dynamic_programming.fibonacci import fibo, fibo_dp

logging.basicConfig(level=logging.INFO, format="%(message)s")


class TestFibonacci(unittest.TestCase):
    def cases(self, fn):
        self.assertEqual(fn(1), 1)
        self.assertEqual(fn(0), 0)
        self.assertEqual(fn(20), 6765)
        self.assertEqual(fn(28), 317811)
        self.assertEqual(fn(40), 102334155)

    def test_fibonacci(self):
        self.cases(fibo)

    def test_dynamic_programming(self):
        self.cases(fibo_dp)
