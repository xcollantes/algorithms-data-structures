"""15. 3Sum

Medium

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.


Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not
matter.


Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.


Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.


Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""


def test_3sum():
    """pytest 3sum.py"""
    result = _3sum([-1, 0, 1, 2, -1, -4])
    expected = [[-1, -1, 2], [-1, 0, 1]]

    # Make it so order does not matter.
    assert set(tuple(sorted(triplet)) for triplet in result) == set(tuple(sorted(triplet)) for triplet in expected)

    assert _3sum([0, 1, 1]) == []
    assert _3sum([0, 0, 0]) == [[0, 0, 0]]


def _3sum(nums: list[int]) -> list[list[int]]:
    """
    [-1,0,1,2,-1,-4] -> [[-1,-1,2],[-1,0,1]]
        [-4, -1, -1, 0, 1, 2]
                     i
                        j
                           k
    """

    nums.sort()  # Sort to be able to shift the left and right pointers to adjust to get to 0.

    print(nums)

    res = []

    for i in range(len(nums)):

        # Skip duplicate elements.
        # Since nums is sorted, adjacent matches will show up next to each
        # other.
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        l = i + 1
        r = len(nums) - 1

        print(f"l {l} r {r}")

        # Two pointer approach.
        while l < r:

            print(f"  l {l} r {r}")

            s = nums[i] + nums[l] + nums[r]

            print(f"sum: {s}")

            if s > 0:
                # if greater than 0, move right pointer to move closer to 0.
                r -= 1

            elif s < 0:
                # if less than 0, move left pointer to move closer to 0.
                l += 1

            else:
                # match
                res.append([nums[i], nums[l], nums[r]])

                # since the array is sorted, identical values will be adjacent

                l += 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1


    return res
