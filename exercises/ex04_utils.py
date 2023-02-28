""" Functions """

__author__ = "730556876"

def all(list: list[int], int: int) -> bool:
    """Searches number list for the example integer"""
    list_idx = 0
    while list_idx < len(list):
        if list[list_idx] != int:
           return False
        list_idx += 1 
    return True
