#!/usr/bin/env python3
"""importing list and Union from typing module"""
from typing import List, Union


mytype = List[Union[int, float]]


def sum_mixed_list(mxd_list: mytype) -> float:
    total = 0
    for item in mxd_list:
        total += item
    return total
