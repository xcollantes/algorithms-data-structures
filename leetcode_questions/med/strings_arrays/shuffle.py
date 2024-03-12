"""
Given an integer array nums, design an algorithm to randomly shuffle the array. All permutations of the array should be equally likely as a result of the shuffling.

Implement the Solution class:

Solution(int[] nums) Initializes the object with the integer array nums.
int[] reset() Resets the array to its original configuration and returns it.
int[] shuffle() Returns a random shuffling of the array.
"""

import copy
import logging
import random


class Shuffle:
    def __init__(self, nums: list[int]) -> None:
        self.nums = nums
        # Technically a shallow copy works since nums is single dimensional
        self.const_nums = copy.deepcopy(nums)

    def reset(self) -> list[int]:
        """Resets the array to its original configuration and returns it."""
        return self.nums

    # This technically works but could possibly repeat.
    #
    # def shuffle(self) -> list[int]:
    #     """Returns a random shuffling of the array."""
    #     return random.sample(self.nums, len(self.nums))

    def shuffle(self) -> list[int]:
        """Returns a random shuffling of the array.

        Uses the Fisher-Yates algorithm.
        """
        answer: list[int] = self.nums[:]  # Shallow copy
        for idx in range(len(answer)):
            logging.info(answer)
            rand_idx = random.randrange(idx, len(answer))
            logging.info(rand_idx)
            answer[rand_idx], answer[idx] = answer[idx], answer[rand_idx]

        return answer
