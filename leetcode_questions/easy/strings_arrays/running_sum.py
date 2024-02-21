"""
Given an array nums. We define a running sum of an array as runningSum[i] =
sum(nums[0]…nums[i]).

Return the running sum of nums.
"""

import logging


def running_sum(nums: list[int]) -> list[int]:
    """Find running sum in list."""
    for idx in range(1, len(nums)):
        nums[idx] = nums[idx - 1] + nums[idx]

    logging.info("%s", nums)
    return nums
