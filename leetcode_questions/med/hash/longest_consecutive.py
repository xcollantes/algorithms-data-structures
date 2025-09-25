"""128. Longest Consecutive Sequence

Medium

Given an unsorted array of integers nums, return the length of the longest
consecutive elements sequence.

You must write an algorithm that runs in O(n) time.


Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.


Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9


Example 3:

Input: nums = [1,0,1,2]
Output: 3


Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
"""


def test_longest_consecutive_simple():
    """pytest longest_consecutive.py"""
    assert longest_consecutive([100, 4, 200, 1, 3, 2]) == 4


def test_longest_consecutive():
    assert longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
    assert longest_consecutive([1, 0, 1, 2]) == 3


def longest_consecutive(nums: list[int]) -> int:

    # Remove dupe values
    # Also good for O(1) lookups
    nums = set(nums)

    h = {}

    maxnum = 0

    for n in nums:

        x = h.get(n - 1, 0)
        y = h.get(n + 1, 0)

        print(f"n: {n} x: {x} y: {y} h: {h}")

        # Calculate the new sequence length ending at n - 1 and starting n + 1,
        # plus 1 for current num

        v = x + y + 1

        h[n - x] = v
        h[n + y] = v
        maxnum = max(maxnum, v)

    return maxnum
