"""374. Guess Number Higher or Lower

Easy

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked (the number
I picked stays the same throughout the game).

Every time you guess wrong, I will tell you whether the number I picked is
higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible
results:

-1: Your guess is higher than the number I picked (i.e. num > pick).
1: Your guess is lower than the number I picked (i.e. num < pick).
0: your guess is equal to the number I picked (i.e. num == pick).
Return the number that I picked.


Example 1:

Input: n = 10, pick = 6
Output: 6


Example 2:

Input: n = 1, pick = 1
Output: 1


Example 3:

Input: n = 2, pick = 1
Output: 1


Constraints:

1 <= n <= 231 - 1
1 <= pick <= n
"""


def guess(num: int, pick: int) -> int:
    """Predefined API for guessing the number.

    Returns:
        int: 0 if the number is equal to the pick, 1 if the number is higher
        than the pick, -1 if the number is lower than the pick.
    """
    if num == pick:
        return 0
    elif num > pick:
        return 1
    else:
        return -1


def test_guess_num():
    """pytest guess_num.py"""
    assert guess_num(10, 6) == 6
    assert guess_num(1, 1) == 1
    assert guess_num(2, 1) == 1


def guess_num(n: int, pick: int) -> int:
    """"""
