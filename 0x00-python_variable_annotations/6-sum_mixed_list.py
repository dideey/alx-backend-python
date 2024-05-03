#!/usr/bin/env python3
"""
importing list and Union from typing module
"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]
                   ) -> float:
    """Takes a list of floats and returns their sum"""
    total = 0
    for item in mxd_list:
        total += item
    return total
