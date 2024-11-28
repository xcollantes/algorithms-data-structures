"""
Given an integer array nums, design an algorithm to randomly shuffle the array. All permutations of the array should be equally likely as a result of the shuffling.

Implement the Solution class:

Solution(int[] nums) Initializes the object with the integer array nums.
int[] reset() Resets the array to its original configuration and returns it.
int[] shuffle() Returns a random shuffling of the array.
"""

import copy
import random


class Shuffle:
    def __init__(self, nums: list[int]) -> None:
        # Track original version with O(1) time complexity.
        self.nums = nums

        # Make sure to use deep copy since the values might still be attached to
        # original data structure.
        self.ORIGINAL = copy.deepcopy(nums)

        # Track position since Fisher-Yates algorithm depends on moving index
        # for each "shuffle" call.
        self.position = 0

    def reset(self) -> list[int]:
        self.nums = self.ORIGINAL
        return self.nums

    def shuffle(self) -> list[int]:
        # Fisher-Yates algorithm chooses a random index and a moving index.
        # The random index and moving index switch values to create a random
        # value each time but a new random set each call.

        random_idx: int = random.randint(
            self.position, len(self.nums) - 1
        )  # - 1 since random includes right value.

        # Switch the random index and moving index.
        self.nums[random_idx], self.nums[self.position] = (
            self.nums[self.position],
            self.nums[random_idx],
        )

        return self.nums
