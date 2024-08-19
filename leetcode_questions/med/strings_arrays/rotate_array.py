"""Given an integer array nums, rotate the array to the right by k steps, where
k is non-negative.
"""


def rotate(nums: list[int], k: int) -> list[int]:
    result = []
    k += 1
    i = 0
    while i < len(nums):
        result.append(nums[k % len(nums)])
        print(f"{result}")
        i += 1
        k += 1

    for i in range(len(nums)):
        nums[i] = result[i]


def rotate_group(nums: list[int], k: int) -> list[int]:
    """Performs rotation in place."""
    k = k % len(nums)  # For when k > len(nums).

    print(f"k after mod: {k}")
    if k != 0:  # For 0 k values.
        nums[:k], nums[k:] = nums[-k:], nums[:-k]

    print(nums)
    return nums


print(rotate_group(nums=[1, 2, 3, 4, 5, 6, 7], k=3))
