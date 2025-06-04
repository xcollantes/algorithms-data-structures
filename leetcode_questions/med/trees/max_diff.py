"""
Given the root of a binary tree, find the maximum value v for which there exist different nodes a and b where v = |a.val - b.val| and a is an ancestor of b.

A node a is an ancestor of b if either: any child of a is equal to b or any child of a is an ancestor of b.
"""

from binary_search_tree.simply_tree import Node


def max_diff(root: Node) -> int:
    return diff(root, root.val, root.val)


def diff(root: Node, min_val: int, max_val: int) -> int:
    """Recursive DFS to find the min and max and the difference."""
    if not root:
        return 0

    # Find the min and max before recursive case
    min_val = min(root.val, min_val)
    max_val = max(root.val, max_val)

    # Leaf case returns the difference
    if not root.left and not root.right:
        return max_val - min_val

    # Recursive case or "on the way up" finds the biggest difference between the
    # two nodes
    return max(diff(root.left, min_val, max_val), diff(root.right, min_val, max_val))


from leetcode_questions.utils.models.leetcode_data_models import (
    Difficulty,
    Metadata,
    Tags,
)

__metadata__ = Metadata(
    tags=[Tags.TREE, Tags.DFS],
    difficulty=Difficulty.MEDIUM,
)
