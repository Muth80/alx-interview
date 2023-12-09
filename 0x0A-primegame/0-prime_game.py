#!/usr/bin/python3

def isWinner(x, nums):
    if not nums:
        return None

    # A list to keep track of prime numbers in nums
    primes = []

    # Check each number in nums to see if it is prime
    for num in nums:
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)

    # A dictionary to keep track of each player's scores
    scores = {"Maria": 0, "Ben": 0}

    # Simulate the game rounds
    for i in range(x):
        current_round = i % 2
        if not primes:
            scores[["Maria", "Ben"][current_round]] += 1
            continue

        prime = primes.pop(0)
        removed = [prime * i for i in range(1, prime + 1)]
        for num in nums[:]:
            if num in removed:
                nums.remove(num)

        scores[["Maria", "Ben"][(current_round + 1) % 2]] += 1

    # Determine the winner
    if scores["Maria"] > scores["Ben"]:
        return "Maria"
    elif scores["Maria"] < scores["Ben"]:
        return "Ben"
    else:
        return None
