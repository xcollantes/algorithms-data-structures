"""Simple node tree which can be used to quickly create trees."""

import logging
from re import I


class Node:
    def __init__(self, val: any, left=None, right=None) -> None:
        self.val = val
        self.left: Node = left
        self.right: Node = right


def inorder_print(node: Node) -> None:
    """Print out node tree."""
    if node:
        inorder_print(node.left)
        logging.info("Node: %s L: %s R:", node.val, node.left.val, node.right.val)
        inorder_print(node.right)


class NodeTree:
    def __init__(self) -> None:
        self.root = Node(None)

    def get_root(self) -> Node:
        return self.root

    def array_to_bst(self, array: list[int]) -> Node:
        """Converts given array to a node tree.

        Args:
            array: List of values to insert.

        Returns:
            Root node of tree.
        """
        self.root.val = array[0]
        for val in array[1:]:
            self._add_node_left_right(self.root, val)

        return self.root

    def array_to_tree_leetcode(self, array: list[int]) -> Node:
        """Fill tree children before moving levels left to right.

        Takes in an array with None value. This is how LeetCode expresses a tree
        with a None child.
        """
        self.root.val = array[0]
        current_node = self.root

        level = 0

        for idx in range(len(array[1:])):
            if idx >= level**2:
                level += 1

            current_node = self._find_parent(current_node, level)

            if current_node.left:
                current_node.left = Node(array[idx])
            else:
                current_node.right = Node(array[idx])

        return self.root

    def _find_parent(self, node: Node, level: int) -> Node:
        """Filling left to right on a specific level.

        The place to start must be found on a certain level.
        """
        if node is None:
            return None
        if level == 1:
            return node

        parent = self._find_parent(node.left, level - 1)
        if parent:
            return parent
        else:
            return self._find_parent(node.right, level - 1)

    def _add_node(self, node: Node, val: any) -> None:
        """Recursively add to tree."""
        if val < node.val:
            if node.left:
                self._add_node(node.left, val)
            else:
                node.left = Node(val)
        if val >= node.val:
            if node.right:
                self._add_node(node.right, val)
            else:
                node.right = Node(val)
