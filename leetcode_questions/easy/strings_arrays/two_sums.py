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


# pytest two_sums.py


def cases(fn):
    assert fn([1, 2], 3) == [0, 1]
    assert fn([2, 3, 5, 14, 543, 23], 25) == [0, 5]
    assert fn([56, 345, 0, 2, 4, 5], 2) == [2, 3]


def test_twosums():
    cases(two_sums)


def test_faster_two_sums():
    cases(faster_two_sums)


from leetcode_questions.utils.models.leetcode_data_models import (
    Difficulty,
    Metadata,
    Tags,
)

__metadata__ = Metadata(
    tags=[Tags.ARRAY, Tags.HASH_TABLE, Tags.TWO_POINTERS],
    difficulty=Difficulty.EASY,
)
