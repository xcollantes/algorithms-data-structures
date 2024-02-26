"""Simple node tree which can be used to quickly create trees."""


class Node:
    def __init__(self, val: any, left=None, right=None) -> None:
        self.val = val
        self.left: Node = left
        self.right: Node = right


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
        for val in array:
            self._add_node(self.root, val)

        return self.root

    def _add_node(self, node: Node, val: any) -> None:
        """Recursively add to tree."""
        # Deal with initial value
        if node.val is None:
            node.val = val

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
