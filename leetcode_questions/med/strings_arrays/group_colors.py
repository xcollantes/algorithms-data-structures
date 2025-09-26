"""75. Sort Colors

Medium

Given an array nums with n objects colored red, white, or blue, sort them
in-place so that objects of the same color are adjacent, with the colors in the
order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and
blue, respectively.

You must solve this problem without using the library's sort function.


Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]


Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]


Constraints:

n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.

Follow up: Could you come up with a one-pass algorithm using only constant extra space?
"""


def test_group_colors_simple():
    """pytest group_colors.py"""
    nums = [2, 0, 2, 1, 1, 0]
    group_colors(nums)
    assert nums == [0, 0, 1, 1, 2, 2]


def test_group_colors():
    """pytest group_colors.py"""
    nums = [2, 0, 1]
    group_colors(nums)
    assert nums == [0, 1, 2]


def group_colors(nums: list[int]) -> list[int]:
    """
    [0, 0, 1, 1, 2, 2]
           r
           w
                 b
    """

    r = 0
    w = 0
    b = len(nums) - 1

    while w <= b:

        # print(f"r: {r} w: {w} b: {b}")
        print()
        for e in nums:
            print(e, end="")
        print()
        print((" " * r) + "r")
        print((" " * w) + "w")
        print((" " * b) + "b")

        # match red
        if nums[w] == 0:

            nums[w], nums[r] = nums[r], nums[w]

            r += 1
            w += 1

        # match white
        elif nums[w] == 1:
            w += 1

        # match blue
        else:
            nums[w], nums[b] = nums[b], nums[w]
            b -= 1
