#!/usr/bin/python3

def isWinner(x, nums):
    # helper function to check if a number is prime
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    # helper function to remove a number and its multiples from the list
    def remove_multiples(nums, n):
        new_nums = []
        for num in nums:
            if num % n != 0:
                new_nums.append(num)
        return new_nums

    # main logic
    winner = "Ben" # assume Ben always goes first
    prime_nums = [num for num in nums if is_prime(num)]

    for num in prime_nums:
        nums = remove_multiples(nums, num)

    # after removing the prime numbers, if there are any left, Maria wins
    if len(nums) != len(prime_nums):
        winner = "Maria"

    return winner



