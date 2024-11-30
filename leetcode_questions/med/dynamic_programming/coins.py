"""322. Coin Change

Medium

You are given an integer array coins representing coins of different
denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that
amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
"""

import logging


def coin(coins: list[int], amount: int) -> int:
    """Return fewest of each coin to make amount."""
    # Create array of min coins to make each index
    min_coins: list[int] = [amount + 1] * (amount + 1)
    logging.info("min_coins: %s", min_coins)

    min_coins[0] = 0

    # Each value is the number of coins needed for that index So index 1 needs 1
    # coin assuming 1 coin is an option in the coins options
    for idx in range(len(min_coins)):
        logging.info("IDX: %s", idx)
        for coin in coins:
            if coin <= idx:
                logging.info(" coin %s is smaller than idx %s", coin, idx)
                logging.info(
                    " new min: %s", min(min_coins[idx], min_coins[idx - coin] + 1)
                )

                # Refer back to the idx - coin then add 1 coin; Iterate the
                # coins until you get min number of coins
                min_coins[idx] = min(min_coins[idx], min_coins[idx - coin] + 1)

                logging.info(" min_coins: %s", min_coins)

    # Check if the amount-th index is still the default set in the beginning
    if min_coins[amount] == amount + 1:
        return -1

    # Return the amount-th index which is the number of coins needed for that
    # amount index
    return min_coins[amount]
