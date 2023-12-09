#!/usr/bin/python3
def isWinner(x, nums):
    # Calculate the next prime number after n
    def nextPrime(n):
        if n <= 1:
            return 2
        if n % 2 == 0:
            n += 1
        while True:
            isPrime = True
            sqrt_n = int(n**0.5) + 1
            for i in range(3, sqrt_n, 2):
                if n % i == 0:
                    isPrime = False
                    break
            if isPrime:
                return n
            n += 2

    # Function to determine the winner of a single round
    def roundWinner(n):
        primeCount = 0
        maxPrime = 0
        for num in nums:
            if num <= n:
                primeCount += 1
                maxPrime = max(maxPrime, num)
        return 'Maria' if primeCount == 1 else 'Ben' if primeCount > 1 else 'None'

    # Initialize the result dictionary
    results = {'Maria': 0, 'Ben': 0, 'None': 0}

    # Iterate through each round and calculate the winner
    for num in nums:
        if num <= 1:
            results['Ben'] += 1
        else:
            n = nextPrime(num)
            winner = roundWinner(n)
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
    import cProfile
    if len(sys.argv) == 3:
        x = int(sys.argv[1])
        nums = list(map(int, sys.argv[2].split(',')))
        cProfile.run('print("Winner: {}".format(isWinner(x, nums)))')
    else:
        print("Usage: {} <number_of_rounds> <comma_separated_numbers>".format(sys.argv[0]))
