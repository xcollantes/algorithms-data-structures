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


def search(target: int, A: list[int]) -> int:
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


# Must be sorted first.
A = [1, 3, 7, 10, 12, 15, 20, 22, 25]

print(f"result: {search(20, A)}")
assert search(20, A) == 6
assert search(10, A) == 3
assert search(40, A) == None
