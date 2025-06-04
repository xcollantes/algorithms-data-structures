"""
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.
"""


def min_cost(cost: list[int]) -> int:
    """Return min cost of steps.

    Bottom-up approach using iterative technique.
    The base case is implicit since we start with a zero list.
    """
    steps: list[int] = [0] * (len(cost) + 1)

    for idx in range(2, len(steps)):
        if cost[idx - 2] > cost[idx - 1]:
            steps[idx] = steps[idx - 1] + cost[idx - 1]
        else:
            steps[idx] = steps[idx - 2] + cost[idx - 2]

    return steps[-1]


from leetcode_questions.utils.models.leetcode_data_models import (
    Difficulty,
    Metadata,
    Tags,
)

__metadata__ = Metadata(
    tags=[Tags.DYNAMIC_PROGRAMMING, Tags.ARRAY],
    difficulty=Difficulty.EASY,
)
