"""Find the height of a tree.

Time complexity: O(n log n)
"""

import logging
from typing import Any, List

logging.basicConfig(level=logging.DEBUG, format="%(message)s")


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None


def main():
    arr: list = [3, 1, 5, 23, 2, 34, 8]

    binary_tree: Node = Node(arr[0])
    for value in arr[1:]:
        insert(value, binary_tree)

    logging.info("Printing tree")
    print_tree(binary_tree)

    assert find_max_depth(binary_tree) + 1, 5

    # + 1 to add starting root node to depth.
    # otherwise you can change the return value for leaf nodes to -1
    logging.info("Find max route: %s", find_max_depth(binary_tree) + 1)


def find_max_depth(root) -> int:
    """Find height or route from root to leaf farthest leaf.

    This is a clean way of writing find height. The limitation is 
    you only know one piece of information: the height by number of nodes.  
    You can't tell which route is farthest. 

    Args:
        root: Node object.

    Returns:
        Integer of height.
    """
    logging.debug("starting on root value: %s", root)
    if root:

        left_depth: int = find_max_depth(root.left)
        right_depth: int = find_max_depth(root.right)

        logging.debug("compare L %s and R %s", left_depth, right_depth)

        if left_depth > right_depth:  # Return max of the L and the R
            return left_depth + 1
        else:
            return right_depth + 1
    else:
        # Leaf nodes will be considered level 0,
        # add one to offset for starting root node at return function
        return 0


def find_max_depth_tracked(root) -> List[Any]:
    """Find height of tree and keep track of nodes.
    """
    longest_path: List[Any] = []
    return _recursive_find_max_depth_tracked(root, longest_path)


def _recursive_find_max_depth_tracked(root: Node, path: List[Any]) -> List[Any]:
    """Recursive calls for finding max depth."""
    if root:

        left_depth: int = _recursive_find_max_depth_tracked(root.left, path)
        right_depth: int = _recursive_find_max_depth_tracked(root.right, path)

        if left_depth > right_depth:
            path.push(root.left.value)
            return left_depth + 1
        else:
            path.push(root.right.value)
            return right_depth + 1
    else:
        return 0


def insert(value, root):
    if root:
        if root.value > value:
            logging.debug("%s is less than root.value: %s", value, root.value)

            if root.left:
                insert(value, root.left)
            else:
                root.left = Node(value)
                logging.debug("Inserted on left")

        if root.value <= value:
            logging.debug("%s is greater than root.value: %s",
                          value, root.value)

            if root.right:
                insert(value, root.right)
            else:
                root.right = Node(value)
                logging.debug("Inserted on right")


def print_tree(root):
    """Preorder print."""
    logging.info(root.value)

    if root.left:
        print_tree(root.left)

    if root.right:
        print_tree(root.right)


if __name__ == "__main__":
    main()
