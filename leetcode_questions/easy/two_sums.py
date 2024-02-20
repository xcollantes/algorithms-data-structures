"""
Given an array of integers nums and an integer target, return indices of the two
numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not
use the same element twice.

You can return the answer in any order.
"""


def two_sums(array: list[int], target: int) -> list[int]:
    for a in range(len(array) - 1):
        b = a + 1
        while b < len(array):
            if array[a] + array[b] == target:
                return [a, b]
            b += 1
