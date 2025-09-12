"""1733. Minimum Number of People to Teach

Medium

On a social network consisting of m users and some friendships between users,
two users can communicate with each other if they know a common language.

You are given an integer n, an array languages, and an array friendships where:

There are n languages numbered 1 through n,
languages[i] is the set of languages the i​​​​​​th​​​​ user knows, and
friendships[i] = [u​​​​​​i​​​, v​​​​​​i] denotes a friendship between the users u​​​​​​​​​​​i​​​​​ and vi.
You can choose one language and teach it to some users so that all friends can
communicate with each other. Return the minimum number of users you need to
teach.

Note that friendships are not transitive, meaning if x is a friend of y and y is
a friend of z, this doesn't guarantee that x is a friend of z.


Example 1:

Input: n = 2, languages = [[1],[2],[1,2]], friendships = [[1,2],[1,3],[2,3]]
Output: 1
Explanation: You can either teach user 1 the second language or user 2 the first language.


Example 2:

Input: n = 3, languages = [[2],[1,3],[1,2],[3]], friendships = [[1,4],[1,2],[3,4],[2,3]]
Output: 2
Explanation: Teach the third language to users 1 and 3, yielding two users to teach.


Constraints:

2 <= n <= 500
languages.length == m
1 <= m <= 500
1 <= languages[i].length <= n
1 <= languages[i][j] <= n
1 <= u​​​​​​i < v​​​​​​i <= languages.length
1 <= friendships.length <= 500
All tuples (u​​​​​i, v​​​​​​i) are unique
languages[i] contains only unique values
"""


def test_min_languages():
    """pytest min_languages.py"""
    assert min_languages(2, [[1],[2],[1,2]], [[1,2],[1,3],[2,3]]) == 1
    assert min_languages(3, [[2],[1,3],[1,2],[3]], [[1,4],[1,2],[3,4],[2,3]]) == 2


def min_languages(n: int, languages: list[list[int]], friendships: list[list[int]]) -> int:

    know = []
    for l in languages:
        know.append(set(l))

    need = set()
    for a1, b1 in friendships:
        a = a1 - 1
        b = b1 - 1

        if know[a] & know[b]:
            continue

        need.add(a)
        need.add(b)

    if not need:
        return 0

    res = float("inf")
    for l in range(1, n + 1):
        count = 0
        for i in need:
            if l not in know[i]:
                count += 1

        res = min(res, count)

    return res



