"""Unit test for min_depth.py."""

import unittest
import logging
from binary_search_tree.min_depth import find_min

from binary_search_tree.simply_tree import Node, NodeTree, inorder_print

logging.basicConfig(level=logging.INFO, format="%(message)s")


class TestMinDepth(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_creation(self):
        vals = [3, 9, 20, None, None, 15, 7]

        tree = NodeTree()
        root = tree.array_to_tree_leetcode(vals)
        inorder_print(root)

    def test_min_depth(self):
        tree = NodeTree()
        root = tree.array_to_tree_leetcode([3, 9, 20, None, None, 15, 7])
        self.assertEqual(find_min(root), 2)

        tree_two = NodeTree()
        root_two = tree_two.array_to_tree_leetcode(
            [2, None, 3, None, 4, None, 5, None, 6]
        )
        self.assertEqual(find_min(root_two), 5)
