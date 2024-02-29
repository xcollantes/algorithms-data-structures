"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

import logging


def climb(n: int) -> int:
    """Return ways to climb stairs of n steps."""
    # Bottom-up approach using iterative
    # With extra element since we want the last count
    count_ways: list[int] = [1] * (n + 1)

    logging.info("Base cases: %s", count_ways)

    for idx in range(2, len(count_ways)):

        # Each step has a number of ways to get there
        # For each new step, add up the ways to there calculated already
        count_ways[idx] = max(count_ways[idx - 2], count_ways[idx - 1]) + 1

    return count_ways[-1]
