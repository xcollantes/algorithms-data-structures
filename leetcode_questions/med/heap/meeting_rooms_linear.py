"""Meeting Rooms Linear

Medium

Given an array of meeting time intervals intervals where
intervals[i] = [starti,endi], return the minimum number of conference rooms
required.

Reduce down to one line.


Constraints:

1 <= intervals.length <= 104
0 <= starti < endi <= 106
"""


def test_meeting_rooms_linear():
    """pytest meeting_rooms.py"""
    assert meeting_rooms_linear([[0, 30], [5, 10], [15, 20]]) == [[0, 30]]
    assert meeting_rooms_linear([[7, 10], [2, 4]]) == [[2, 4], [7, 10]]
    assert meeting_rooms_linear([[13, 15], [1, 13]]) == [[1, 13], [13, 15]]


import heapq


def meeting_rooms_linear(intervals: list[list[int]]) -> int:
    """
    [[0,30],[5,10],[15,20]]

    0 [0,                          30]
    1    [5,   10]
    2               [15,    20]

    cur = 0
    """

    times = []

    for s, e in intervals:

        times.append((s, 1, "s"))
        times.append((e, 0, "e"))

    heapq.heapify(times)

    print(times)

    stack = []
    res = []

    while times:
        t = heapq.heappop(times)

        # Stack will only have starts.

        # start case needs to check if stack has in-progress meeting.
        # if none, then mark a new timeline.
        if t[2] == "s":
            if not stack:
                res.append([t[0], None])

            stack.append(t[2])

        # when an end time is encountered, check if a start time is already in
        # stack, if so, pop it.

        # then add to the last result as end time.

        elif t[2] == "e":

            _ = stack.pop()

            if res:
                res[-1][1] = t[0]

        print(f"t {t} stack {stack} res {res}")

    print(f"answer {res}")
    return res
