"""Unit test for stock_span.py."""

import unittest
import logging

from leetcode_questions.med.stacks_queues.stock_span import StockSpan

logging.basicConfig(level=logging.INFO, format="%(message)s")


class TestStockSpan(unittest.TestCase):
    def test_stock_span(self):
        stock = StockSpan()
        self.assertEqual(stock.next(100), 1)
        self.assertEqual(stock.next(80), 1)
        self.assertEqual(stock.next(60), 1)
        self.assertEqual(stock.next(70), 2)
        self.assertEqual(stock.next(60), 1)
        self.assertEqual(stock.next(75), 4)
        self.assertEqual(stock.next(85), 6)
