"""Merge sort.

Popular in real use where an array is split up into multiple sub-problems known
as divide and conquer.

Time complexity O(n * log n) since the list is split by O(log n). Then from
there, the combining stage is O(n).

Space complexity O(1) since there is a key value held outside of the array.

Divide and conquer technique with time complexity of O(n log n). The array is
broken down to its most atomic parts then put back together but the parts are
compared when reorganized.

The mid element is chosen using `mid: int = len(input) // 2` where the `//` will
return the floor divide of the operands. This is true for Python3.

Time complexity: O(n log n). Breaks down the list of elements and makes
comparisons for each atomic value.

https://www.programiz.com/dsa/merge-sort
"""


def merge_recursive(input: list) -> None:
    """Merge sort to return sorted list.

    In place where result is changing the original list.

    Recursive version where function is called with splitting up until atomic
    values then combined; sort as list is merged.
    """
    if len(input) <= 1:
        return input

    # Split phase until each element is in atomic elements
    mid: int = len(input) // 2  # Integer divide

    left = input[:mid]
    right = input[mid:]

    # Left split until end of tree.  Then continue with function to split on
    # right.
    print(f"LEFT: {left}")
    merge_recursive(left)

    print(f"RIGHT: {right}")
    merge_recursive(right)

    left_idx = right_idx = result_idx = 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            input[result_idx] = left[left_idx]
            left_idx += 1
        else:
            input[result_idx] = right[right_idx]
            right_idx += 1

        result_idx += 1

    # Append the rest of array when only left or only right remain
    while left_idx < len(left):
        input[result_idx] = left[left_idx]
        left_idx += 1
        result_idx += 1

    while right_idx < len(right):
        input[result_idx] = right[right_idx]
        right_idx += 1
        result_idx += 1

    return input
