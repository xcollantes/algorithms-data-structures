"""Simple node tree which can be used to quickly create trees."""

import logging


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

    def array_to_tree(self, array: list[int]) -> Node:
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

    def _add_node_left_right(self, node: Node, val: any) -> None:
        """Fill tree children before moving levels left to right."""
        if node.val is None:
            return
        if node.left is None:
            node.left = Node(val)
        if node.right is None:
            node.right = Node(val)
        elif node.left and node.right:
            self._add_node_left_right(node.left, val)
