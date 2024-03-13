#!/usr/bin/python3

def sieve_of_eratosthenes(limit):
    """
    Generate all prime numbers up to a given limit using the Sieve of Eratosthenes algorithm.

    :param limit: The upper limit for prime numbers.
    :return: A list of prime numbers.
    """
    primes = [True] * (limit + 1)
    primes[0], primes[1] = False, False

    for num in range(2, int(limit**0.5) + 1):
        if primes[num]:
            for multiple in range(num*num, limit + 1, num):
                primes[multiple] = False

    return [num for num in range(2, limit + 1) if primes[num]]

def is_prime(num):
    """
    Check if a number is prime.

    :param num: The number to check.
    :return: True if the number is prime, False otherwise.
    """
    if num < 2:
        return False
    primes = sieve_of_eratosthenes(int(num**0.5) + 1)
    return any(num % prime == 0 for prime in primes)

def isWinner(x, nums):
    """
    Determine the winner of the game given the number of rounds and the set of consecutive integers.

    :param x: The number of rounds.
    :param nums: An array of n consecutive integers.
    :return: The name of the player with the most wins, or None if there's a tie.
    """
    wins = {'Maria': 0, 'Ben': 0}

    for _ in range(x):
        current_nums = nums[:_ + 1]
        player = 'Maria'

        while any(num > 1 for num in current_nums):
            can_remove = False
            for i, num in enumerate(current_nums):
                if is_prime(num) and num > 1:
                    current_nums = [n for n in current_nums if n % num != 0]
                    can_remove = True
                    break

            if not can_remove:
                break

            player = 'Ben' if player == 'Maria' else 'Maria'

        if len(current_nums) == 1 and is_prime(current_nums[0]):
            wins[player] += 1

    max_wins = max(wins.values())
    if max_wins == 0:
        return None
    return list(filter(lambda key: wins[key] == max_wins, wins.keys()))[0]
