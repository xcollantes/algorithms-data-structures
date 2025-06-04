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


# pytest running_sum.py


def test_running_sum():
    assert running_sum([1, 2, 3, 4]) == [1, 3, 6, 10]
    assert running_sum([1, 1, 1, 1, 1]) == [1, 2, 3, 4, 5]
    assert running_sum([3, 1, 2, 10, 1]) == [3, 4, 6, 16, 17]
    assert running_sum([1]) == [1]
    assert running_sum([]) == []


from leetcode_questions.utils.models.leetcode_data_models import (
    Difficulty,
    Metadata,
    Tags,
)

__metadata__ = Metadata(
    tags=[Tags.ARRAY, Tags.PREFIX_SUM],
    difficulty=Difficulty.EASY,
)
