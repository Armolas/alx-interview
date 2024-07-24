#!/usr/bin/python3
"""Making Change"""


def makeChange(coins, total):
    """ Makes change
    """
    if total <= 0:
        return 0

    # Initialize the dp array with total + 1,
    # which is larger than any possible number of coins
    dp = [total + 1] * (total + 1)
    dp[0] = 0  # Base case: 0 coins are needed to make the total 0

    # Iterate over all amounts from 1 to total
    for i in range(1, total + 1):
        # Check every coin to find the minimum number of coins for amount i
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still total + 1,
    # it means we cannot form the amount with the given coins
    return dp[total] if dp[total] != total + 1 else -1
