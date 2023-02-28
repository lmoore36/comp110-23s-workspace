""" Functions """

__author__ = "730556876"

def all(list: list[int], int: int) -> bool:
    """Searches number list for the example integer"""
    list_idx = 0
    while list[list_idx] == int:
        list_idx += 1
        if list[len(list)-1] == int:
            return True
    return False
