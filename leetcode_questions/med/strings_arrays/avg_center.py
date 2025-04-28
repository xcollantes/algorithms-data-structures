"""
You are given a 0-indexed array nums of n integers, and an integer k.

The k-radius average for a subarray of nums centered at some index i with the
radius k is the average of all elements in nums between the indices i - k and i
+ k (inclusive). If there are less than k elements before or after the index i,
then the k-radius average is -1.

Build and return an array avgs of length n where avgs[i] is the k-radius average
for the subarray centered at index i.

The average of x elements is the sum of the x elements divided by x, using
integer division. The integer division truncates toward zero, which means losing
its fractional part.

For example, the average of four elements 2, 3, 1, and 5 is (2 + 3 + 1 + 5) / 4
= 11 / 4 = 2.75, which truncates to 2.
"""

import logging


def test_avg_center():
    cases(avg_center)


def test_faster():
    cases(faster_avg)


def cases(fn):
    assert fn([2, 1, 3, 1, 0, 2, 1], 2) == [-1, -1, 1, 1, 1, -1, -1]
    assert fn([7, 4, 3, 9, 1, 8, 5, 2, 6], 3) == [-1, -1, -1, 5, 4, 4, -1, -1, -1]
    assert fn([100000], 0) == [100000]
    assert fn([8], 100000) == [-1]


def avg_center(nums: list[int], k: int) -> list[int]:
    """Return list of averages."""
    result: list[int] = [-1 for _ in range(len(nums))]

    for idx in range(k, len(nums) - k):
        result[idx] = sum(nums[idx - k : idx + k + 1]) // ((k * 2) + 1)
        logging.info("Calculate: %s", result[idx])

    return result


def faster_avg(nums: list[int], k: int) -> list[int]:
    result: list[int] = [-1 for _ in range(len(nums))]
    window_size = (k * 2) + 1
    window_sum = 0

    for idx in range(len(nums)):
        window_sum += nums[idx]
        if idx >= window_size:
            # Move the window forward by removing the first value in the array
            window_sum -= nums[idx - window_size]

        if idx >= window_size - 1:
            # Index is at end of window
            # Then determine the value of "center" of window with idx - k
            result[idx - k] = window_sum // window_size

    return result
