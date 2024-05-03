#!/usr/bin/env python3
"""importing from typing module"""
from typing import Union, Any, Sequence


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """takes a list of elements and returns the first element"""	
    if lst:
        return lst[0]
    else:
        return None