"""Unit test for design_stack.py."""

import unittest
import logging

from leetcode_questions.med.stacks_queues.design_stack import MinStack

logging.basicConfig(level=logging.INFO, format="%(message)s")


class TestDesignStack(unittest.TestCase):
    def test_design_stack(self):
        minStack = MinStack()
        minStack.push(-2)
        minStack.push(0)
        minStack.push(-3)
        self.assertEqual(minStack.getMin(), -3)
        minStack.pop()
        self.assertEqual(minStack.top(), 0)
        self.assertEqual(minStack.getMin(), -2)
