"""56. Merge Intervals

Medium

Given an array of intervals where intervals[i] = [starti, endi], merge all
overlapping intervals, and return an array of the non-overlapping intervals that
cover all the intervals in the input.


Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].


Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.


Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
"""


def test_merge_intervals():
    """pytest merge_intervals.py"""
    assert merge_intervals([[0, 30], [5, 10], [15, 20]]) == [[0, 30]]
    assert merge_intervals([[7, 10], [2, 4]]) == [[2, 4], [7, 10]]
    assert merge_intervals([[13, 15], [1, 13]]) == [[1, 15]]
    assert merge_intervals([[1, 4], [0, 0]]) == [[0, 0], [1, 4]]


import heapq


def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    """
    [[0,30],[5,10],[15,20]]

    0 [0,                          30]
    1    [5,   10]
    2               [15,    20]

    prev = [0, 30]

    5,10
    """

    intervals.sort(key=lambda x: x[0])

    print(intervals)

    res = []

    prev = intervals[0]
    for time in intervals[1:]:

        # if current start is before last end
        if time[0] <= prev[1]:

            # update the end to longer ending
            prev[1] = max(prev[1], time[1])

        else:

            res.append(prev)

            # restart with new mark
            # this would mean the current start is after the prev end time
            prev = time

        print(f"time {time} prev {prev} res {res}")

    res.append(prev)

    print(f"answer {res}")

    return res
