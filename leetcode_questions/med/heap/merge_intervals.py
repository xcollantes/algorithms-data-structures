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
    assert merge_intervals([[1, 4], [0, 0]]) == [[[0, 0], [1, 4]]]


import heapq


def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    """
    [[0,30],[5,10],[15,20]]

    0 [0,                          30]
    1    [5,   10]
    2               [15,    20]

    cur = 0
    """

    times = []
    # turn to heap

    for s, e in intervals:

        # 1 for if same number. use start first.
        times.append((s, 1, "s"))
        times.append((e, 0, "e"))

    heapq.heapify(times)

    stack = []
    # if stack is empty, add popped start and cur (end) to res

    res = []

    while times:

        t = heapq.heappop(times)

        if t[2] == "s":

            if not stack:

                # case where new mark starts
                # Check if we can extend the previous interval.
                if res and res[-1][1] is not None and res[-1][1] >= t[0]:
                    # Previous interval ends at or after this start, so extend it.
                    res[-1][1] = None  # Mark as open again.
                else:
                    # Start a new interval.
                    res.append([t[0], None])

            stack.append(t)

        elif t[2] == "e":

            if stack:
                _ = stack.pop()

                if not stack:
                    # No more active intervals, close current interval.
                    res[-1][1] = t[0]

        print(f"t {t} stack {stack} res {res}")

    # return list of coors
    print(res)
    return res
