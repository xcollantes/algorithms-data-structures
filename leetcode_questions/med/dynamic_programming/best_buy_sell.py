"""
You are given an array prices where prices[i] is the price of a given stock on the ith day, and an integer fee representing a transaction fee.

Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.

Note:

You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
The transaction fee is only charged once for each stock purchase and sale.
"""

import logging


def max_profit(prices: list[int], fee: int) -> int:
    """Return best max profit."""

    min_price = prices[0] + fee
    max_profit = 0

    for price in prices:

        if min_price < price:
            max_profit += price - min_price
            min_price = price
        elif price + fee < min_price:
            min_price = price + fee

    return max_profit
