""" Functions """

__author__ = "730556876"

def all(num_list: list[int], example_int: int) -> bool:
    """Searches number list for the example integer"""
    list_idx = 0
    while list_idx < len(num_list):
        if num_list[list_idx] == example_int:
            return True
        list_idx += 1
    return False
