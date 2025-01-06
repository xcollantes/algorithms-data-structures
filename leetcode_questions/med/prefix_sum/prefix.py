"""560. Subarray Sum Equals K

Medium

Given an array of integers nums and an integer k, return the total number of
subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.


Example 1:

Input: nums = [1,1,1], k = 2
Output: 2


Example 2:

Input: nums = [1,2,3], k = 3
Output: 2


Constraints:

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107
"""


def subarray_sum(nums: list[int], k: int) -> int:

    count = 0
    prefix = 0
    sums = {0: 1}

    for num in nums:

        # Prefix will continuously accumulate values.
        prefix += num

        print(f"num: {num}; count: {count}; prefix: {prefix}; sums: {sums}")

        if prefix - k in sums:

            print(f"prefix - k: {prefix - k}")
            count += sums[prefix - k]

        # Increment the count of sum.
        sums[prefix] = sums.get(prefix, 0) + 1

        print(f"sums[prefix] increment: {sums[prefix]}")

    return count
