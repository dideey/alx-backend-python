#!/usr/bin/env python3
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Takes a list of floats and returns their sum"""
    items = 0
    for item in input_list:
        items += item
    return items
