"""Unit test for min_depth.py."""

import unittest
import logging

from binary_search_tree.simply_tree import Node

logging.basicConfig(level=logging.INFO, format="%(message)s")


class TestMinDepth(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_creation(self):
        vals = [3, 9, 20, None, None, 15, 7]
        self.root = Node(vals[0])
        for v in vals[1:]:
            


    def test_min_depth(self):
        self.assertEqual("", "")
