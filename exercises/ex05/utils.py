"""Docstring"""

__author__ = "730556876"

def only_evens(numbers: list[int]) -> int:
    """Return even numbers from a list"""
    even_list: int = 0
    for x in numbers:
        if x % 2 == 0:
            even_list += x
    return even_list

        