#!/usr/bin/python3

def sieve_of_eratosthenes(n):
    """Efficiently generates prime numbers up to n"""
    numbers = [True] * (n + 1)
    numbers[0] = numbers[1] = False
    p = 2
    while p * p <= n:
        if numbers[p]:
            for i in range(p * p, n + 1, p):
                numbers[i] = False
        p += 1
    return [num for num, is_prime in enumerate(numbers) if is_prime]


def game_round(n):
    """Simulates one round of the game, returning the winner"""
    numbers = list(range(1, n + 1))
    primes = sieve_of_eratosthenes(n)  # Calculate primes only once

    player = "Maria"
    while primes:
        prime = primes.pop(0)  # Find next available prime
        for i in range(0, len(numbers), prime):
            numbers[i] = 0  # Mark prime and its multiples as removed

        player = "Maria" if player == "Ben" else "Ben"

    return "Ben" if player == "Maria" else "Maria"  # Last player unable to play loses


def isWinner(x, nums):
    """Plays x rounds and determines the overall winner"""
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = game_round(n)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None  # Tie

# Example usage (from your provided test case)
if __name__ == "__main__":
     print("Winner: {}".format(isWinner(3, [4, 5, 1])))

