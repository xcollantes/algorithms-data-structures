"""Unit test for simply_tree.py."""

import unittest
import logging

from binary_search_tree.simply_tree import Node, NodeTree

logging.basicConfig(level=logging.INFO, format="%(message)s")


class TestSimplyTree(unittest.TestCase):
    def is_equal(self, tree_one: Node, tree_two: Node) -> bool:
        """Returns true if two trees are equal."""

    def preorder_traverse(self, node: Node) -> list:
        """Traverse whole tree in pre-order."""
        values = []
        if node:
            logging.info("Visiting node: %s", node.val)

            values.append(node.val)
            values += self.preorder_traverse(node.left)
            values += self.preorder_traverse(node.right)

        return values

    def test_single_node(self):
        n = Node(10)
        self.assertEqual(n.val, 10)
        self.assertEqual(n.left, None)
        self.assertEqual(n.right, None)

        m = Node(10, 20, 30)
        self.assertEqual(m.val, 10)
        self.assertEqual(m.left, 20)
        self.assertEqual(m.right, 30)

    def test_array(self):
        vals = [5, 1, 2, 3, 0]
        result_tree = NodeTree()
        result_tree.array_to_tree(vals)
        logging.info(self.preorder_traverse(result_tree.get_root()))

        # result_tree.array_to_tree(vals)

        # self.assertTrue(self.is_equal(expected_tree, result_tree))
