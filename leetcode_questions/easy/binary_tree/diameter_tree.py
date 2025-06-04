"""543. Diameter of Binary Tree

Easy

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two
nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges
between them.

Constraints:

The number of nodes in the tree is in the range [1, 104].
-100 <= Node.val <= 100
"""


class TreeNode:
    def __init__(self, val: int = 0, left: int = None, right: int = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self.dia = 0


    def diameter_binary_tree(self, root: TreeNode) -> int:
        self.depth(root)
        return self.dia

    def depth(self, root: TreeNode) -> int:
        print(f"DEPTH: root: {root}")

        left = 0
        right = 0

        if root.left:
            left = self.depth(root.left)

        if root.right:
            right = self.depth(root.right)

        self.dia = max(self.dia, left + right)

        return max(left, right) + 1


