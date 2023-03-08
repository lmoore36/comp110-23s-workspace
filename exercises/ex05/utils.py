"""Utils functions."""

__author__ = "730556876"


def only_evens(numbers: list[int]) -> int:
    """Returns even numbers from a list."""
    evens: list[int] = []
    for x in numbers:
        if x % 2 == 0:
            evens.append(x)
    return evens


def concat(list1: list[int], list2: list[int]) -> int:
    """Adds two lists together."""
    final_list: list[int] = list1 + list2
    return final_list


def sub(list: list[int], idx1: int, idx2: int) -> int:
    """Subsets a list within a range."""
    if idx1 < 0:
        idx1 = 0
    if idx2 > len(list):
        idx2 = len(list)
    subset_list: list[int] = []
    while idx1 < idx2:
        subset_list.append(list[idx1])
        idx1 += 1
    return subset_list