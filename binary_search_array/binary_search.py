"""Array implementation of binary search.

## Example

Looking for value of 20

len = 8

mid = 0 + 8 // 2 = 4
[1, 3, 7, 10, 12, 15, 20, 22, 25]
 L             M              R


[1, 3, 7, 10, 12, 15, 20, 22, 25]
               M  L           R
mid = 5 + 8 // 2 = 6


[1, 3, 7, 10, 12, 15, 20, 22, 25]
                  L   M       R
"""

import unittest


def search_iterative(target: int, A: list[int]) -> int:
    """Returns the index where element found None otherwise"""

    # Initiate left and right indices as edges of the array.
    left = 0
    right = len(A) - 1

    # 1. As long as the left and right don't cross, keep calculating mid value.
    while left <= right:
        print(f"LEFT: {left} RIGHT: {right}")

        # 2. Mid is calculated as long as target not found.
        # Keep cutting the scope by half until the target element is found.
        mid = (right + left) // 2

        print(f"New mid: {mid}")

        # 3. If the target is either lower or higher than the mid, then shift the
        # left and right indices to focus on a subsection of the array.

        # This is why we want to have a sorted array before starting since we'll
        # have a direction where the target element is given the "current"
        # location.
        # This is the downside of binary search.

        # If the mid index is the value, then return index and finish search.
        if target == A[mid]:
            return mid
        elif target < A[mid]:
            right = mid - 1
        elif target > A[mid]:
            left = mid + 1

    return None


def recursive(s: list[int], left: int, right: int, target: int) -> int:
    """Recursive approach retaining the array passed in."""

    print(f"left: {left} right: {right}")

    if left <= right:

        mid = (left + right) // 2

        print(f"mid: {mid}")

        if s[mid] == target:
            return mid

        elif target < s[mid]:
            return recursive(s, left, mid - 1, target)

        elif target > s[mid]:
            return recursive(s, mid + 1, right, target)

    else:
        return None


def recursive_partitions(s: list[int], target: int) -> int:
    """Recursive approach passing in partitions.

    Instead of the whole array, partitions of the array are passed in. There is
    no longer a need for left and right pointers but there is no way to track
    indices if that is the required result.
    """

    print(f"s: {s}")

    # Base case where not found.
    if not s:
        return None

    mid = len(s) // 2

    print(f"mid: {mid}")

    if s[mid] == target:
        return s[mid]

    elif target < s[mid]:
        return recursive_partitions(s[:mid], target=target)

    elif s[mid] < target:
        return recursive_partitions(s[mid:], target=target)


class Test(unittest.TestCase):

    # Must be sorted first.
    A = [1, 3, 7, 10, 12, 15, 20, 22, 25]

    def test_iterative(self) -> None:
        self.assertEqual(search_iterative(20, self.A), 6)
        self.assertEqual(search_iterative(10, self.A), 3)
        self.assertEqual(search_iterative(40, self.A), None)

    def test_recursive(self) -> None:
        self.assertEqual(recursive(self.A, 0, len(self.A) - 1, 20), 6)
        self.assertEqual(recursive(self.A, 0, len(self.A) - 1, 10), 3)
        self.assertEqual(recursive(self.A, 0, len(self.A) - 1, 40), None)

    def test_partitions(self) -> None:
        # Cannot return the index but the value instead.
        self.assertEqual(recursive_partitions(self.A, 20), 20)
        self.assertEqual(recursive_partitions(self.A, 10), 10)
        self.assertEqual(recursive_partitions(self.A, 40), None)
