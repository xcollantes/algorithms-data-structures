"""973. K Closest Points to Origin

Medium

Given an array of points where points[i] = [xi, yi] represents a point on the
X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance
(i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique
(except for the order that it is in).


Example 1:

Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]

Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].


Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.


Constraints:
1 <= k <= points.length <= 104
-104 <= xi, yi <= 104
"""

import heapq
import math


def test_k_closest():
    """pytest k_closest.py"""
    assert k_closest([[1, 3], [-2, 2]], 1) == [[-2, 2]]
    assert k_closest([[3, 3], [5, -1], [-2, 4]], 2) == [[3, 3], [-2, 4]]


def k_closest(points: list[list[int]], k: int) -> list[list[int]]:
    """
    Since we want the k smallest, use heap.

    Calculate the Euclidean distance and rank.
    """

    h = []

    for x, y in points:

        d = math.sqrt(x**2 + y**2)
        h.append((d, x, y))

    heapq.heapify(h)

    smallest = heapq.nsmallest(k, h)
    print(smallest)
    return [[x, y] for d, x, y in smallest]
