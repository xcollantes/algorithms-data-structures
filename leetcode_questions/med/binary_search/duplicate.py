"""287. Find the Duplicate Number

Medium

Given an array of integers nums containing n + 1 integers where each integer is
in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and using only
constant extra space.


Example 1:

Input: nums = [1,3,4,2,2]
Output: 2


Example 2:

Input: nums = [3,1,3,4,2]
Output: 3


Example 3:

Input: nums = [3,3,3,3,3]
Output: 3


Constraints:

1 <= n <= 105
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which
appears two or more times.


Follow up:

How can we prove that at least one duplicate number must exist in nums?
Can you solve the problem in linear runtime complexity?
"""


def test_bin_duplicate():
    """pytest duplicate.py"""
    assert bin_duplicate([1, 3, 4, 2, 2]) == 2
    assert bin_duplicate([3, 1, 3, 4, 2]) == 3
    assert bin_duplicate([3, 3, 3, 3, 3]) == 3
    assert bin_duplicate([1, 1]) == 1


def test_sort_duplicate():
    """pytest duplicate.py"""
    assert sort_duplicate([1, 3, 4, 2, 2]) == 2
    assert sort_duplicate([3, 1, 3, 4, 2]) == 3
    assert sort_duplicate([3, 3, 3, 3, 3]) == 3
    assert sort_duplicate([1, 1]) == 1


def test_duplicate():
    """pytest duplicate.py"""
    assert duplicate([1, 3, 4, 2, 2]) == 2
    assert duplicate([3, 1, 3, 4, 2]) == 3
    assert duplicate([3, 3, 3, 3, 3]) == 3
    assert duplicate([1, 1]) == 1


def bin_duplicate(nums: list[str]) -> int:
    """
    [1, 3, 4, 2, 2]
           m

    """

    l = 0
    r = len(nums) - 1

    while l < r:

        m = (l + r) // 2

        print(f"l {l} r {r} m {m}")

        count = 0
        for num in nums:
            if num <= m:
                count += 1

        if count > m:
            r = m
        else:
            l = m + 1

    return l


def sort_duplicate(nums: list[str]) -> int:
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i - 1] == nums[i]:
            return nums[i]


def duplicate(nums: list[str]) -> int:
    """This will timeout in Leetcode due to wanting a more efficient algo."""
    for l in range(len(nums)):

        for r in range(l + 1, len(nums)):

            print(f"l {l} r {r}")

            if nums[l] == nums[r]:
                return nums[l]
