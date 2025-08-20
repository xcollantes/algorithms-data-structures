"""253. Meeting Rooms II

Medium

Given an array of meeting time intervals intervals where
intervals[i] = [starti,endi], return the minimum number of conference rooms
required.


Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2

Example 2:

Input: intervals = [[7,10],[2,4]]
Output: 1


Constraints:

1 <= intervals.length <= 104
0 <= starti < endi <= 106
"""


def test_meeting_rooms():
    """pytest meeting_rooms.py"""
    assert meeting_rooms([[0, 30], [5, 10], [15, 20]]) == 2
    assert meeting_rooms([[7, 10], [2, 4]]) == 1
    assert meeting_rooms([[13, 15], [1, 13]]) == 1


import heapq


def meeting_rooms(intervals: list[list[int]]) -> int:
    """
    [[0,30],[5,10],[15,20]]

    0 [0,                          30]
    1    [5,   10]
    2               [15,    20]

    cur = 0 2
    max = 2
    """

    # order by min heap to iterate
    times = []

    for i, se in enumerate(intervals):

        # by start or end and meeting number

        # there is as case where the start and end time are the same.
        # process the end event first
        times.append((se[0], 1, i))
        times.append((se[1], 0, i))

    heapq.heapify(times)

    print(times)

    cur_occ = set()
    max_occ = 0

    while times:

        print(f"times {times}")

        t = heapq.heappop(times)

        print(f"t {t}")

        if t[2] in cur_occ:
            print(f"pop {t[2]}")

            cur_occ.remove(t[2])
        else:
            print(f"add {t[2]}")
            cur_occ.add(t[2])

        print(f"cur {cur_occ}")

        max_occ = max(len(cur_occ), max_occ)
        print()

    print(f"ans {max_occ}")

    return max_occ
