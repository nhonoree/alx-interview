#!/usr/bin/python3
"""
Module that defines minOperations function
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed
    to result in exactly n 'H' characters.

    Parameters:
    - n: int

    Returns:
    - int: minimum number of operations, or 0 if impossible
    """
    if n < 2:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
