#!/usr/bin/python3

def makeChange(coins, total):
    # If total is 0 or less, return 0
    if total <= 0:
        return 0

    # Create a list to store the fewest number of coins needed for each amount from 0 to total
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed for total = 0

    # Iterate through all amounts from 1 to total
    for i in range(1, total + 1):
        # Iterate through all available coin values
        for coin in coins:
            # If the current coin value is less than or equal to the current amount
            if coin <= i:
                # Update the fewest number of coins needed for the current amount
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # If it's not possible to make the total using available coins, return -1
    if dp[total] == float('inf'):
        return -1

    return dp[total]  # Return the fewest number of coins needed for the total

