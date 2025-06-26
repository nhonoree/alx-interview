#!/usr/bin/python3

def sieve(n):
    """Return a list of primes up to n using Sieve of Eratosthenes"""
    is_prime = [True for _ in range(n + 1)]
    is_prime[0:2] = [False, False]  # 0 and 1 are not prime
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for multiple in range(i*i, n + 1, i):
                is_prime[multiple] = False
    return is_prime

def isWinner(x, nums):
    """Determine the winner of the Prime Game"""
    if x < 1 or not nums:
        return None

    max_n = max(nums)
    primes = sieve(max_n)

    # Count primes up to each number from 0 to max_n
    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if primes[i] else 0)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_count[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
