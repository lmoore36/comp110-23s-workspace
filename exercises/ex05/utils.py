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
    final_list: list[int] = list1 + list2
    return final_list

def sub(list: list[int], idx1: int, idx2: int) -> int:
    idx2 = idx2 - 1
    for list in range(list[idx1], list[idx2]):
        return list


      

