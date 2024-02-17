"""Heap sort.

Recursive tree algorithm used to store values in order (either Min Heap or Max
Heap).  Min Heap stores the lowest values at the top of the tree near the root 
where Max is the opposite and stores highest values at the top. 

A heap is a binary tree structure if: 
    1. the heap is a complete binary tree
    2. each node is greater than their children (less than if Max Heap) 

Time complexity: 
    Insert: O(log n)
    Extract min or max: O(log n)

Sources: 
    - https://www.programiz.com/dsa/heap-data-structure 
    - https://www.programiz.com/dsa/heap-sort 
    - https://www.geeksforgeeks.org/python-program-for-heap-sort 
"""

import logging
import copy

logging.basicConfig(level=logging.DEBUG, format="%(message)s")


def main():
    logging.info("Heap sort")
    a_list: list = [1, 12, 9, 5, 6, 10]
    unsorted_list: list = copy.deepcopy(a_list)

    logging.info("Create a binary tree from an array")
    # array_to_tree(a_list)

    max_heap_sort_an_array(a_list)
    logging.info("heap sorted: %s", a_list)
    assert a_list == sorted(unsorted_list)


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left_child = None
        self.right_child = None


def max_heap_sort_an_array(arr: list):
    """Build Max Heap.

    Args:
        arr: Unsorted array.
    """
    # Run heapify on all elements of array by rearranging array
    # We're only using length of array divided by 2 minus 1 since these are
    # the roots and all other elements are leaves.
    # Positions in the tree to array can be seen as
    #      index 0
    #          /   \
    #         1     2
    #        / \   / \
    #       3  4  5  6
    #
    # Indices 0, 1, 2 in the array are roots and 3, 4, 5, 6 are leaves
    for index in range(len(arr) // 2, -1, -1):
        logging.debug("value to heapify: root: %s on index: %s",
                      arr[index], index)
        _heapify(arr, len(arr), index)

    # Extract the top element and build return array.
    #
    # We now have a Max Heap with the largest value on top of the heap.
    #   1. Remove the top node and place value into an array.
    #      Conceptually we are "removing" but really we are
    #      adjusting the index minus 1.
    #   2. Perform heapify on the root element
    for index in range(len(arr) - 1, 0, -1):
        logging.debug("traverse heap: %s", arr)
        arr[index], arr[0] = arr[0], arr[index]
        _heapify(arr, index, 0)


def _heapify(arr: list, size: int, root_idx: int) -> None:
    """Find position for a node value using Heap Sort.

    Args:
        arr (list): Array of data.
        size (int): Length of array. 
        root_idx (int): Current node to check if max.
    """
    largest_idx = root_idx  # Initialize as root as largest
    left_idx = 2 * root_idx + 1
    right_idx = 2 * root_idx + 2

    # If left is in range and left child is larger than root
    if left_idx < size and arr[left_idx] > arr[root_idx]:
        largest_idx = left_idx

    if right_idx < size and arr[right_idx] > arr[largest_idx]:
        largest_idx = right_idx

    if largest_idx is not root_idx:
        # Swap if the largest node is no longer root
        arr[root_idx], arr[largest_idx] = arr[largest_idx], arr[root_idx]

        # Call recursively to keep checking if root is largest
        _heapify(arr, size, largest_idx)


def array_to_tree(arr: list) -> Node:
    """Convert list to Binary Tree.

    Args:
        arr (list): Array of integers.

    Returns:
        Root of Node tree.
    """
    if arr == []:
        return Node(None)

    root: Node = Node(arr[0])
    if len(arr) == 1:
        return root

    for i in arr[1:]:
        logging.debug("Adding node %s to root %s", i, root.value)
        _insert(root, i)
        logging.debug("")


def _insert(root: Node, value: int) -> None:
    """Insert values from an array into a tree.

    This is not a Heap because this will naively insert new
    values on the left.  

    To improve this, the tree must be traversed multiple times to 
    see which node has only one child and add the new node on the 
    parent with only one left child.  
    In the case where there is a Perfect Tree as in all leaves are filled
    and the leaves are at the same level, then we can add to the new level
    on the left of the leftmost leaf. 

    Args:
        root (Node): Some node to recursively look at. 
        value (int): Some integer. 
    """
    logging.debug("At node %s | left: %s | right: %s",
                  root.value, root.left_child, root.right_child)

    if root.left_child is None:
        root.left_child = Node(value)
        logging.debug("added new node %s to left child", root.left_child.value)

    elif root.right_child is None:
        root.right_child = Node(value)
        logging.debug("added new node %s to right child",
                      root.right_child.value)

    else:
        _insert(root.left_child, value)

    return


if __name__ == "__main__":
    main()
