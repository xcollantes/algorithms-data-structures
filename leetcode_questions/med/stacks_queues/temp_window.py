"""
Given an array of integers temperatures represents the daily temperatures,
return an array answer such that answer[i] is the number of days you have to
wait after the ith day to get a warmer temperature. If there is no future day
for which this is possible, keep answer[i] == 0 instead.
"""


def daily_temps(temps: list[int]) -> list[int]:
    stack = []
    answer = [0] * len(temps)

    for idx in range(len(temps)):
        while stack and temps[stack[-1]] < temps[idx]:
            last_idx = stack.pop()
            answer[last_idx] = idx - last_idx

        stack.append(idx)

    return answer


from leetcode_questions.utils.models.leetcode_data_models import (
    Difficulty,
    Metadata,
    Tags,
)

__metadata__ = Metadata(
    tags=[Tags.STACK, Tags.ARRAY],
    difficulty=Difficulty.MEDIUM,
)
