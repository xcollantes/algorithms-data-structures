"""
Given a binary array nums and an integer k, return the maximum number of
consecutive 1's in the array if you can flip at most k 0's.
"""


def ones(nums: list[int], k: int):
    left: int = 0
    for right in range(len(nums)):
        if nums[right] == 0:
            k -= 1

        if k < 0:
            if nums[left] == 0:
                # We're not actually changing the 0 to 1, just keeping track of
                # the k count.
                k += 1

            # Move left pointer one.
            left += 1

    return right - left + 1  # Plus 1 since right is not inclusive.


from leetcode_questions.utils.models.leetcode_data_models import (
    Difficulty,
    Metadata,
    Tags,
)

__metadata__ = Metadata(
    tags=[Tags.ARRAY, Tags.SLIDING_WINDOW],
    difficulty=Difficulty.MEDIUM,
)
