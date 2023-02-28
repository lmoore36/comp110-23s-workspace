""" Functions and List Exercises. """

__author__ = "730556876"

def all(input: list[int], int: int) -> bool:
    """Searches number list for the example integer"""
    list_idx = 0
    while list_idx < len(input):
        if input[list_idx] != int:
           return False
        list_idx += 1 
    return True

def max(input: list[int]) -> int:
    """Returns the largest number in a list"""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    high_number = input[0]
    list_idx = 0
    while list_idx < len(input):
        if high_number < input[list_idx]:
            high_number = input[list_idx]
        list_idx += 1
    return high_number

def is_equal(input_1: list[int], input_2: list[int]) -> bool:
    """Checks two lists for equality"""
    list_idx = 0
    while list_idx < len(input_1):
        if input_1[list_idx] != input_2[list_idx]:
           return False
        list_idx += 1 
    return True
