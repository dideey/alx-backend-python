#!/usr/bin/env python3
from typing import List
"""importing list"""

mytype = tuple[int, float]
def sum_mixed_list(mxd_list: mytype) -> float:
    total = 0
    for item in mxd_list:
        total += item
    return total
