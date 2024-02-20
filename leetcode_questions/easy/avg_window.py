"""
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum
average value and return this value. Any answer with a calculation error less
than 10-5 will be accepted.
"""

import logging
from numpy import mean


def avg_window(nums: list[int], k: int) -> float:
    """Return highest average."""
    # if len(nums) <= 1:
    #     return nums[0]

    front_idx: int = 0
    end_idx: int = front_idx + k
    avgs: list[float] = []

    while end_idx <= len(nums):
        avgs.append(mean(nums[front_idx:end_idx]))
        logging.info("%s %s %s", front_idx, end_idx, avgs)

        front_idx += 1
        end_idx += 1

    logging.info(avgs)
    return max(avgs)


def avg_window_optimized(nums: list[int], k: int) -> float:
    """Previous function will timeout due to inefficiency when calculating
    extremely large test case.
    """
    window_sum = sum(nums[:k])
    answer = window_sum

    for front_idx in range(1, len(nums) - k + 1):
        # Track sum
        window_sum = window_sum - nums[front_idx - 1] + nums[front_idx + k - 1]
        answer = max(window_sum, answer)

    # Perform division operation at end
    return answer / k
