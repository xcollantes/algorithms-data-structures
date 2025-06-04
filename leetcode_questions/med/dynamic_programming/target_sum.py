"""494. Target Sum

Medium

You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and
'-' before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and
concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates
to target.


Example 1:

Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be
target 3.

-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3


Example 2:

Input: nums = [1], target = 1
Output: 1

Constraints:

1 <= nums.length <= 20
0 <= nums[i] <= 1000
0 <= sum(nums[i]) <= 1000
-1000 <= target <= 1000
"""

from collections import defaultdict


def test_target_sum():
    """pytest target_sum.py"""
    assert target_sum([1, 1, 1, 1, 1], 3) == 5
    # assert target_sum([1], 1) == 1
    # assert target_sum([1, 2, 3, 4, 5], 3) == 3
    # assert target_sum([1, 2, 3, 4, 5], 1) == 3


def target_sum(nums: list[int], target: int) -> int:
    d = defaultdict(int)

    print(f"d: {d}")

    def dfs(i=0, total=0):
        print(f"dfs: i {i} total {total}")

        # Current state.
        key = (i, total)

        if key not in d:
            print(f"key {key} not in {d}")

            # Base case where we reached end.
            if i == len(nums):
                print(f"i == len")

                if total == target:
                    return 1
                else:
                    return 0

            else:

                # We explore both the addition and subtraction.
                #
                # At some point, the iteration will end at the last of nums.
                #      (0, 0)
                #     /      \
                # +1 /        \ -1
                # (1, 1)     (1, -1)
                #
                # (2, 2) from +1
                # (2, 0) from -1

                addition = dfs(i + 1, total + nums[i])
                subtraction = dfs(i + 1, total - nums[i])

                print(f"result {addition} + {subtraction}")

                d[key] = addition + subtraction

        print(f"return {d[key]}")
        return d[key]

    return dfs(0, 0)


from leetcode_questions.utils.models.leetcode_data_models import (
    Difficulty,
    Metadata,
    Tags,
)

__metadata__ = Metadata(
    tags=[Tags.DYNAMIC_PROGRAMMING, Tags.ARRAY, Tags.DFS],
    difficulty=Difficulty.MEDIUM,
)
