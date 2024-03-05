#!/usr/bin/python3
"""
This module contains the function makeChange to determine the
fewest number of coins needed to meet a given amount total.
"""

def makeChange(coins, total):
    if total <= 0:
        return 0
    
    # Initialize the dp array with inf values for all totals up to the target total
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: no coins needed to make total of 0

    # Build up the dp array from smallest total to the target total
    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return -1 if dp[total] == float('inf') else dp[total]

# Your command line tests can go below, but they won't be executed when importing this module.
if __name__ == "__main__":
    print(makeChange([1, 2, 25], 37))
    print(makeChange([1256, 54, 48, 16, 102], 1453))
