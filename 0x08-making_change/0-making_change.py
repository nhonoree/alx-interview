#!/usr/bin/python3
"""
0-making_change.py
Determines the fewest number of coins needed to meet a given amount total
"""


def makeChange(coins, total):
    if total <= 0:
        return 0

    # Initialize a list with total + 1 elements, set to a large value (total + 1 is safe upper bound)
    dp = [total + 1] * (total + 1)
    dp[0] = 0  # base case: 0 coins to make 0

    for amount in range(1, total + 1):
        for coin in coins:
            if coin <= amount:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != total + 1 else -1
