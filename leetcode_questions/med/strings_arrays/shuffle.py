"""
Given an integer array nums, design an algorithm to randomly shuffle the array. All permutations of the array should be equally likely as a result of the shuffling.

Implement the Solution class:

Solution(int[] nums) Initializes the object with the integer array nums.
int[] reset() Resets the array to its original configuration and returns it.
int[] shuffle() Returns a random shuffling of the array.
"""


class Shuffle:
    def __init__(self, nums: list[int]) -> None:
        self.nums = nums
        self.const_nums = nums

    def reset(self) -> list[int]:
        """Resets the array to its original configuration and returns it."""

    def shuffle(self) -> list[int]:
        """Returns a random shuffling of the array."""
