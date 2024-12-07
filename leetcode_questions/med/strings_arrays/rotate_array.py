"""189. Rotate Array

Given an integer array nums, rotate the array to the right by k steps, where
k is non-negative.
"""


def rotate(nums: list[int], k: int) -> list[int]:
    # Track.
    # We know how big the result will be.
    result = [0] * len(nums)

    # Iterate.
    for i in range(len(nums)):
        # `(i + k)` is the amount current index plus the shift amount.
        offset = i + k

        # `% len(nums)` for when we reach the end of the nums array.
        result[offset % len(nums)] = nums[i]

        print(result)

    # Return.
    return result


def rotate_group(nums: list[int], k: int) -> list[int]:
    """Performs rotation in place."""

    # For when k > len(nums).
    k = k % len(nums)

    print(f"k after mod: {k}")
    if k != 0:  # For 0 k values.

        # Array sections can be replaced if they are the same length.
        #
        # The right value is always exclusive.
        #
        # `nums[-k:]` is length of 3; same as `nums[:k]`
        # `nums[:-k]` is length of 4; same as `nums[k:]`
        nums[:k], nums[k:] = nums[-k:], nums[:-k]

    print(nums)
    return nums


print(rotate_group(nums=[1, 2, 3, 4, 5, 6, 7], k=3))
