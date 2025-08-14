"""518. Coin Change II

Medium

You are given an integer array coins representing coins of different
denominations and an integer amount representing a total amount of money.

Return the number of combinations that make up that amount. If that amount of
money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

The answer is guaranteed to fit into a signed 32-bit integer.


Example 1:

Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1


Example 2:

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
Example 3:

Input: amount = 10, coins = [10]
Output: 1


Constraints:

1 <= coins.length <= 300
1 <= coins[i] <= 5000
All the values of coins are unique.
0 <= amount <= 5000
"""


def test_coins_ii():
    """pytest coins_ii.py"""
    assert coins_ii(5, [1, 2, 5]) == 4
    assert coins_ii(3, [2]) == 0
    assert coins_ii(10, [10]) == 1


def coins_ii(amount: int, coins: list[int]) -> int:
    dyn = [0] * (amount + 1)
    dyn[0] = 1  # Init 1 way to make 0; no coins

    print(dyn)

    # We iterate on the coins for permutations.
    for coin in coins:

        # Starting from the coin to the end, we see if we can add the current
        # coin.
        for i in range(coin, amount + 1):

            print(f"i {i} ")

            # dyn[i] represents the number of ways to make that number

            # If you can make amount (i - coin) in some number of ways, then
            # adding the current coin to each of those ways gives you additional
            # ways to make amount i.

            # Example:

            # Say coin = 2, i = 5, and dyn[3] = 2 (meaning there are 2 ways to
            # make amount 3)

            # - dyn[5] += dyn[3] means "add 2 more ways to make amount 5"
            # - Those 2 new ways are: each way to make 3, plus the coin of value
            #   2

            # The += is crucial:

            # - We don't use = because we want to accumulate all possible ways
            # - Previous iterations may have already found some ways to make
            #   amount i using other coins
            # - We're adding the new ways we just discovered to the existing
            #   count

            dyn[i] += dyn[i - coin]

            # The dyn[i - coin] refers back to the number of ways before the
            # current coin.

        print(dyn, end="\n")

    print(dyn[amount])

    return dyn[amount]
