"""179. Largest Number

Medium

Given a list of non-negative integers nums, arrange them such that they form the
largest number and return it.

Since the result may be very large, so you need to return a string instead of an
integer.


Example 1:

Input: nums = [10,2]
Output: "210"


Example 2:

Input: nums = [3,30,34,5,9]
Output: "9534330"


Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 109
"""


def test_longest_digit_str():
    """pytest longest_digit_str.py"""
    assert longest_digit_str(nums=[10, 2]) == "210"
    assert longest_digit_str(nums=[3, 30, 34, 5, 9]) == "9534330"
    assert longest_digit_str(nums=[0, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == "1098765432"


def longest_digit_str(nums: list[int]) -> str:
    """
    """
