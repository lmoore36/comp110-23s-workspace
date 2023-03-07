"""Docstring"""

__author__ = "730556876"

def only_evens(numbers: list[int]) -> int:
    """Return even numbers from a list"""
    evens: list[int] = []
    for x in numbers:
        if x % 2 == 0:
            evens.append(x)
    return evens

def concat(list1: list[int], list2: list[int]) -> int:
    """Returns numbers that appear in both lists"""
    list1.append(list2)
    return list1

def sub(list: list[int], idx1: int, idx2: int) -> int:
    range_list: list[int] = []
    for x in range(idx1, idx2):
        range_list.append(x)
    return range_list


      

