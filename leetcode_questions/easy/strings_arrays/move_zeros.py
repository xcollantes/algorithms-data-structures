"""283. Move Zeroes

Easy

Given an integer array nums, move all 0's to the end of it while maintaining the
relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:

Input: nums = [0]
Output: [0]

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1

Follow up: Could you minimize the total number of operations done?
"""


def test_move_zeros():
    nums = [0, 1, 0, 3, 12]
    move_zeros(nums)
    assert nums == [1, 3, 12, 0, 0]

    nums = [0]
    move_zeros(nums)
    assert nums == [0]

    nums = [1]
    move_zeros(nums)
    assert nums == [1]

    nums = []
    move_zeros(nums)
    assert nums == []


def move_zeros(nums: list[int]) -> None:
    """
    2 pointers. When R finds non-zero, switch with L, then move L + 1.

    [1, 3, 12, 0, 12]
           l
                 r
    [1, 3, 12, 0, 0]
    """
    l = 0
    for r in range(len(nums)):
        if nums[r] != 0:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
