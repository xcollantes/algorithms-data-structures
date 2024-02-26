"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.
"""

from binary_search_tree.simply_tree import Node, NodeTree


def find_min(root: Node) -> int:
    """Return min depth of binary tree."""
    if root is None:
        return 0

    if root.left and root.right:
        return min(find_min(root.left), find_min(root.right)) + 1
    elif root.left:
        return find_min(root.left) + 1
    elif root.right:
        return find_min(root.right) + 1
    else:
        return 1
