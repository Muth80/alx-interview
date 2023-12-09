#!/usr/bin/python3

def isWinner(x, nums):
    # Function to determine if a number is prime
    def isPrime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    # Function to determine the winner of a single round
    def roundWinner(n):
        primeCount = sum(1 for num in nums if num <= n and isPrime(num))
        return 'Maria' if primeCount % 2 == 1 else 'Ben'

    # Initialize the result dictionary
    results = {'Maria': 0, 'Ben': 0}

    # Iterate through each round and calculate the winner
    for num in nums:
        winner = roundWinner(num)
        results[winner] += 1

    # Determine the player with the most wins
    if results['Maria'] > results['Ben']:
        return 'Maria'
    elif results['Maria'] < results['Ben']:
        return 'Ben'
    else:
        return 'None'

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 3:
        x = int(sys.argv[1])
        nums = list(map(int, sys.argv[2].split(',')))
        print("Winner: {}".format(isWinner(x, nums)))
    else:
        print("Usage: {} <number_of_rounds> <comma_separated_numbers>".format(sys.argv[0]))

