"""Unit test for min_depth.py."""

import unittest
import logging

from binary_search_tree.simply_tree import Node, NodeTree, inorder_print

logging.basicConfig(level=logging.INFO, format="%(message)s")


class TestMinDepth(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_creation(self):
        vals = [3, 9, 20, None, None, 15, 7]

        tree = NodeTree()
        root = tree.array_to_tree(vals)
        inorder_print(root)

    def test_min_depth(self):
        self.assertEqual("", "")
