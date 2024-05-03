#!/usr/bin/env python3
"""
    gives the multiplies of a float
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
        the function that multiplies a float
    """
    def multiply(n: float) -> float:
        """
            returns the multiplies of a float
        """
        return n * multiplier

    return multiply