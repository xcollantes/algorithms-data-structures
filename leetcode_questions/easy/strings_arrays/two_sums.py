"""1. Two Sum

https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target, return indices of the two
numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not
use the same element twice.

You can return the answer in any order.
"""


def two_sums(array: list[int], target: int) -> list[int]:
    """O(n^2)"""
    for a in range(len(array) - 1):
        b = a + 1
        while b < len(array):
            if array[a] + array[b] == target:
                return [a, b]
            b += 1


def faster_two_sums(array: list[int], target: int) -> list[int]:
    """O(n)"""

    # {complement: index}
    comp_map = {}

    for i in range(len(array)):
        complement = target - array[i]

        # Check if missing complement has been seen.
        if complement in comp_map:
            return [comp_map[complement], i]

        comp_map[array[i]] = i

    return []
