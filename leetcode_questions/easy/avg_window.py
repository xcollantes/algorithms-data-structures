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
    # if len(nums) <= 1: return nums[0]

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

    Prefix sum is a technique that can be used on arrays (of numbers). The idea
    is to create an array prefix where prefix[i] is the sum of all elements up
    to the index i (inclusive). For example, given nums = [5, 2, 1, 6, 3, 8], we
    would have prefix = [5, 7, 8, 14, 17, 25].

    When a subarray starts at index 0, it is considered a "prefix" of the array.
    A prefix sum represents the sum of all prefixes.

    Prefix sums allow us to find the sum of any subarray in � ( 1 ) O(1). If we
    want the sum of the subarray from i to j (inclusive), then the answer is
    prefix[j] - prefix[i - 1], or prefix[j] - prefix[i] + nums[i] if you don't
    want to deal with the out of bounds case when i = 0.

    This works because prefix[i - 1] is the sum of all elements before index
    i. When you subtract this from the sum of all elements up to index j, you
    are left with the sum of all elements starting at index i and ending at
    index j, which is exactly what we are looking for.
    """
    window_sum = sum(nums[:k])
    answer = window_sum

    for front_idx in range(1, len(nums) - k + 1):
        # Track sum
        window_sum = window_sum - nums[front_idx - 1] + nums[front_idx + k - 1]
        answer = max(window_sum, answer)

    # Perform division operation at end
    return answer / k
