#!/usr/bin/python3

def makeChange(coins, total):
    """
    Finds the minimum number of coins needed using a greedy approach.

    Args:
        coins: A list of available coin denominations.
        total: The target amount to make change for.

    Returns:
        The minimum number of coins needed, or -1 if change cannot be made.
    """

    num_coins = 0
    coins.sort(reverse=True)  # Sort coins in descending order

    for coin in coins:
        while total >= coin:
            num_coins += 1
            total -= coin

    return num_coins if total == 0 else -1
