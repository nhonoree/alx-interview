#!/usr/bin/python3
"""
0-prime_game.py
Maria and Ben play a game where they pick prime numbers and remove them
and their multiples. The player who can't make a move loses.
"""


def sieve(n):
    """Generates a list of booleans where True means prime number"""
    is_prime = [False, False] + [True] * (n - 1)
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return is_prime


def isWinner(x, nums):
    """
    Determines the winner of the game after x rounds.
    Maria always goes first.
    Returns: name of the player with the most wins or None
    """
    if not nums or x < 1:
        return None

    max_n = max(nums)
    is_prime = sieve(max_n)

    # Precompute number of primes up to each i
    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if is_prime[i] else 0)

    maria_score = 0
    ben_score = 0

    for n in nums:
        if prime_count[n] % 2 == 0:
            ben_score += 1
        else:
            maria_score += 1

    if maria_score > ben_score:
        return "Maria"
    elif ben_score > maria_score:
        return "Ben"
    return None
