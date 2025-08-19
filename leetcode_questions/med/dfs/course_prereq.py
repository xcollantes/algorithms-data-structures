"""207. Course Schedule

Medium

There are a total of numCourses courses you have to take, labeled from 0 to
numCourses - 1. You are given an array prerequisites where prerequisites[i] =
[ai, bi] indicates that you must take course bi first if you want to take course
ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first
take course 1.  Return true if you can finish all courses. Otherwise, return
false.


Example 1:

Input: numCourses = 2, prerequisites = [[1,0]] Output: true Explanation: There
are a total of 2 courses to take.  To take course 1 you should have finished
course 0. So it is possible.


Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]] Output: false Explanation:
There are a total of 2 courses to take.  To take course 1 you should have
finished course 0, and to take course 0 you should also have finished course 1.
So it is impossible.


Constraints:

1 <= numCourses <= 2000 0 <= prerequisites.length <= 5000
prerequisites[i].length == 2 0 <= ai, bi < numCourses All the pairs
prerequisites[i] are unique.
"""

from collections import defaultdict


def test_can_finish_simple():
    """pytest can_finish.py"""
    # assert can_finish(2, [[1, 0]]) == True
    # assert can_finish(2, [[1, 0], [0, 1]]) == False
    assert can_finish(4, [[1, 0], [2, 1], [3, 2]]) == True


def test_can_finish_complex():
    # Test case with no prerequisites
    assert can_finish(3, []) == True
    # Test case with single course
    assert can_finish(1, []) == True
    # Complex dependency chain (linear)
    assert can_finish(4, [[1, 0], [2, 1], [3, 2]]) == True
    # Complex dependency chain with multiple prerequisites
    assert can_finish(5, [[1, 0], [2, 0], [3, 1], [3, 2], [4, 3]]) == True
    # Complex dependency chain with cycle
    assert can_finish(4, [[1, 0], [2, 1], [3, 2], [0, 3]]) == False
    # Multiple prerequisites for same course
    assert can_finish(4, [[3, 0], [3, 1], [3, 2]]) == True
    # Complex branching structure with cycle
    assert (
        can_finish(
            7, [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 3], [6, 4], [6, 5], [1, 6]]
        )
        == False
    )
    # Large number of courses with complex dependencies
    assert (
        can_finish(
            10, [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6], [8, 7], [9, 8]]
        )
        == True
    )
    # Large number of courses with cycle at the end
    assert (
        can_finish(
            10,
            [
                [1, 0],
                [2, 1],
                [3, 2],
                [4, 3],
                [5, 4],
                [6, 5],
                [7, 6],
                [8, 7],
                [9, 8],
                [0, 9],
            ],
        )
        == False
    )
    print("All test cases passed!")


def can_finish(num_courses: int, prerequisites: list[list[int]]) -> bool:

    # map each course with prereqs
    # there may be more than one.
    prereq = defaultdict(list)
    for course, pre in prerequisites:
        prereq[course].append(pre)

    print(f"prereq {prereq}")

    done = set()

    def dfs(c) -> bool:
        """Checks for cyclical patterns."""

        print(f"dfs {c}")

        # no prereq
        if not prereq[c]:
            return True

        # circle found
        if c in done:
            return False

        done.add(c)

        for p in prereq[c]:
            if not dfs(p):
                return False

        prereq[c] = []
        return True

    for num in range(num_courses):

        print(f"starting {num}")

        if not dfs(num):
            return False

    return True
