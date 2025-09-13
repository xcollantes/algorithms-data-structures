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


def test_min_simple_languages():
    """pytest min_languages.py"""
    assert min_languages(2, [[1], [2], [1, 2]], [[1, 2], [1, 3], [2, 3]]) == 1


def test_min_complex_languages():
    """pytest min_languages.py"""
    assert (
        min_languages(3, [[2], [1, 3], [1, 2], [3]], [[1, 4], [1, 2], [3, 4], [2, 3]])
        == 2
    )
    assert (
        min_languages(
            17,
            [
                [4, 7, 2, 14, 6],
                [15, 13, 6, 3, 2, 7, 10, 8, 12, 4, 9],
                [16],
                [10],
                [10, 3],
                [4, 12, 8, 1, 16, 5, 15, 17, 13],
                [4, 13, 15, 8, 17, 3, 6, 14, 5, 10],
                [11, 4, 13, 8, 3, 14, 5, 7, 15, 6, 9, 17, 2, 16, 12],
                [4, 14, 6],
                [16, 17, 9, 3, 11, 14, 10, 12, 1, 8, 13, 4, 5, 6],
                [14],
                [7, 14],
                [17, 15, 10, 3, 2, 12, 16, 14, 1, 7, 9, 6, 4],
            ],
            [
                [4, 11],
                [3, 5],
                [7, 10],
                [10, 12],
                [5, 7],
                [4, 5],
                [3, 8],
                [1, 5],
                [1, 6],
                [7, 8],
                [4, 12],
                [2, 4],
                [8, 9],
                [3, 10],
                [4, 7],
                [5, 12],
                [4, 9],
                [1, 4],
                [2, 8],
                [1, 2],
                [3, 4],
                [5, 10],
                [2, 7],
                [1, 7],
                [1, 8],
                [8, 10],
                [1, 9],
                [1, 10],
                [6, 7],
                [3, 7],
                [8, 12],
                [7, 9],
                [9, 11],
                [2, 5],
                [2, 3],
            ],
        )
        == 4
    )


def min_languages(
    n: int, languages: list[list[int]], friendships: list[list[int]]
) -> int:

    # Convert each user's language list to a set for O(1) intersection operations
    # languages are 1-indexed, sets allow fast membership testing and intersection
    know = []
    for l in languages:
        know.append(set(l))

    # Find all users who are in friendships where friends can't communicate
    # (i.e., they share no common language)
    need = set()
    for a, b in friendships:

        # Convert from 1-indexed to 0-indexed (users are 1-based in input)
        a -= 1
        b -= 1

        # Check if users a and b share any common language using set intersection
        # If intersection is non-empty, they can communicate, skip this friendship
        if know[a] & know[b]:
            continue

        # If no common language, both users need to learn a language to communicate
        # Add both users to the set of users who need language instruction
        need.add(a)
        need.add(b)

    # If no users need to be taught (all friendships already work), return 0
    if not need:
        return 0

    print(f"need: {need}")
    print(f"know: {know}")

    # For each possible language (1 to n), calculate how many users in 'need'
    # would need to be taught that specific language
    res = float("inf")
    for lang in range(1, n + 1):

        print(f"language: {lang}")

        count = 0

        # Count how many users in the 'need' set don't already know language l
        for i in need:

            if lang in know[i]:

                print(f"user {i} knows language {lang}")

                # If the user does not know language l, increment the count by
                # 1. This count represents the number of users who would need to
                # learn language l to enable communication in their friendships.
                count += 1

        # Keep track of the minimum count across all languages

        print(f"count: {count}")
        res = min(res, count)

    # Return the minimum number of users that need to be taught any single language
    return res
