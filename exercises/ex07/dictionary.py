"""Dictionary Functions to Practice Unit Tests."""

__author__ = "730556876"


def invert(dict1: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values of a dictionary."""
    new_dict: dict[str, str] = {}

    for key, value in dict1.items():
        if value in new_dict:
            raise KeyError(f'{value} is already in new_dict!')
        else:
            new_dict[value] = key
    return new_dict


def favorite_color(dict1: dict[str, str]) -> str:
    """Determines which favorite color is most common."""
    most_common: dict[str, int] = {}

    for name, color in dict1.items():
        if color not in most_common:
            most_common[color] = 1
        else:
            most_common[color] += 1
    
    most_common_color: str = ""
    most_common_count: int = 0

    print(most_common)

    for color, count in most_common.items():
        if most_common[color] > most_common_count:
            most_common_color = color
            most_common_count = most_common[color]
    return most_common_color


def count(list1: list[str]) -> dict[str, int]:
    """Counts the number of each digit."""
    count_dict: dict[str, int] = {}

    for item in list1:
        if item not in count_dict:
            count_dict[item] = 1
        else:
            count_dict[item] += 1
    return count_dict