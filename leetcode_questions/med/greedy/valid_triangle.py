"""611. Valid Triangle Number

Medium

Given an integer array nums, return the number of triplets chosen from the array
that can make triangles if we take them as side lengths of a triangle.


Example 1:

Input: nums = [2,2,3,4]
Output: 3
Explanation: Valid combinations are:
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3


Example 2:

Input: nums = [4,2,3,4]
Output: 4


Constraints:

1 <= nums.length <= 1000
0 <= nums[i] <= 1000
"""


def test_valid_triangle():
    """pytest valid_triangle.py"""
    assert valid_triangle([2, 2, 3, 4]) == 3
    assert valid_triangle([4, 2, 3, 4]) == 4


def valid_triangle(nums: list[int]) -> int:
    """"""
    nums.sort()

    total = 0

    for longest in range(len(nums) - 1, 1, -1):

        print(f"l {l} r {r} ")

        l = 0
        r = longest - 1

        while l < r:

            print(f"    {nums[l]} + {nums[r]} = {nums[l] + nums[r]} > {nums[longest]}")

            if nums[l] + nums[r] > nums[longest]:
                total += r - l
                r -= 1
            else:
                l += 1

    print(f"total: {total}")

    return total
