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
    """
    What is a triangle?
    two of the sides must be larger than the 3rd because think of collapsable
    tent poles with 3 breaks: if two of the sides are smaller than 3rd, they
    won't reach each other.

    [2, 2, 3, 4]
     l
        r
           L

    [2, 2, 3, 4] sorted
     0  1  2  3  (indices)

    longest = 3 (value 4):
    l=0, r=2: nums[0] + nums[2] > nums[3] → 2 + 3 > 4 ✓
              total += r - l = 2 - 0 = 2 (counts both (2,3,4) combinations)
              r moves to 1
    l=0, r=1: nums[0] + nums[1] > nums[3] → 2 + 2 > 4 ✗
              l moves to 1, now l == r, exit

    longest = 2 (value 3):
    l=0, r=1: nums[0] + nums[1] > nums[2] → 2 + 2 > 3 ✓
              total += r - l = 1 - 0 = 1 (counts (2,2,3))
              r moves to 0, now l > r, exit

    Total: 2 + 1 = 3 triangles




    """
    nums.sort()
    # sort so the longest values are on the right where we start with longest
    # because the 3rd pointer can be fixed if the other 2 are smaller than the
    # longest

    total = 0

    for longest in range(len(nums) - 1, 1, -1):

        # iterate over each element as the longest

        print(f"longest: {nums[longest]}")

        l = 0
        r = longest - 1

        while l < r:

            print(f"    {nums[l]} + {nums[r]} = {nums[l] + nums[r]} > {nums[longest]}")

            # check for valid triangle
            if nums[l] + nums[r] > nums[longest]:
                total += r - l
                r -= 1
            else:
                l += 1

    print(f"total: {total}")

    return total
