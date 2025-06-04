"""50. Pow(x, n)

Medium

Implement pow(x, n), which calculates x raised to the power n (i.e., xn).


Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000


Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100


Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25


Constraints:

-100.0 < x < 100.0
-231 <= n <= 231-1
n is an integer.
Either x is not zero or n > 0.
-104 <= xn <= 104
"""


def power(x: float, n: int) -> float:

    if n >= 0:
        # If exponent positive.
        return _pow(x, n)

    else:
        # If exponent negative, treat as negative calculation.
        return 1 / _pow(x, -n)


def _pow(base: float, ex: int) -> float:

    print(f"base: {base} ex: {ex}")

    # Base case.
    if ex == 0:
        return 1

    # Avoid doing the same calculation twice.
    temp = _pow(base, ex // 2)
    print(f"temp: {temp}")

    if ex % 2 == 0:
        result = temp * temp

        print(f"return: {result}")
        return result
    else:
        result = temp * temp * base

        print(f"return: {result}")
        return result


from leetcode_questions.utils.models.leetcode_data_models import (
    Difficulty,
    Metadata,
    Tags,
)

__metadata__ = Metadata(
    tags=[Tags.MATH, Tags.RECURSION],
    difficulty=Difficulty.MEDIUM,
)
