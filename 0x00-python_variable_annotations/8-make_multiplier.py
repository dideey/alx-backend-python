#!/usr/bin/env python3
"""make_multiplier func"""


def make_multiplier(multiplier: float) -> callable:
    """function that returns a func"""

    def multiply(n: float) -> float:
        """multiplies two floats"""
        return n * multiplier

    return multiply
