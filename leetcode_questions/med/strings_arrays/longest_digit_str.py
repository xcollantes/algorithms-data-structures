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
    assert longest_digit_str(nums=[0, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == "9876543210"


def longest_digit_str(nums: list[int]) -> str:
    """
    """

    arr = [str(n) for n in nums]

    # print(arr)

    # Python will sort alphabetically.
    # So numbers as string will be [10, 2, 21, 22]

    # at first i tried padding each string with "9". as many as the largest
    # placed number. so if the longest number is 100: [100, 199, 299]

    # but using 9 has limit with [3, 30, 34, 5, 9]
    # [39, 30, 34, 59, 90] -> [30, 34, 39, 59, 90]
    # where 34 (34) is before 3 (39)

    arr.sort(reverse=True, key=lambda x: x * 10)

    # for a in arr:
    #     print(f"{a * 10}: {a}")

    if arr[0] == "0":
        return "0"

    print(arr)

    return "".join(arr)

