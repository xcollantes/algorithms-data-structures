"""268. Missing Number

Find missing number.

Given an array nums containing n distinct numbers in the range [0, n], return
the only number in the range that is missing from the array.
"""

import logging

logging.basicConfig(level=logging.DEBUG, format="%(message)s")


def missing_num(nums: list[int]) -> int:
    """Naive answer running at 1476 ms and taking 17.73 MB.

    https://freeimage.host/i/J16J9Np
    """
    counter: int = 0
    while counter <= len(nums):
        logging.info("counter: %s", counter)
        if counter not in nums:
            return counter
        counter += 1


def optimized_missing_num(nums: list[int]) -> int:
    """O(1) answer since list sorting is in place.
    113 ms and taking 17.86 MB.

    https://freeimage.host/i/J16HpHv
    """
    nums.sort()

    for idx in range(len(nums)):
        if nums[idx] is not idx:
            return idx

    return len(nums)


# pytest missing_num.py


def test_missing():
    assert missing_num([3, 0, 1]) == 2
    assert missing_num([0, 1]) == 2
    assert missing_num([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8


def test_optimized():
    assert optimized_missing_num([3, 0, 1]) == 2
    assert optimized_missing_num([0, 1]) == 2
    assert optimized_missing_num([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8
