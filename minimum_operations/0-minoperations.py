#!/usr/bin/python3
"""Calculates the minimum operations required to reach n characters."""


def minOperations(n):
    """Return the fewest Copy All and Paste operations to produce n Hs."""
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
