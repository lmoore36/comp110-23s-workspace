"""Practice Functions for Quiz 2!"""

def odd_and_even (list1: list[int]) -> list[int]:
    """Return a list of odd numbers with an even index."""
    i: int = 0
    list2: list[int] = []

    while i < len(list1):
        if list1[i] % 2 == 1 and i % 2 == 0:
            list2.append(list1[i])
        i += 1
    
    return list2

def value_exists (dict1: dict[str,int], value: int) -> bool:
    """Checks is a dictionary contains a specific value.""" 
    exists: bool = False
   
    for i in dict1:
        if dict1[i] == value:
            exists = True
    return exists 

def short_words (list1: list[str]) -> list[str]:
    """Reeturns a list with words shorter than five characters."""
    i: int = 0
    while i < len(list1):
        if len(list1[i]) > 5:
            print(f"{list1[i]} is too long!")
            list1.pop(i)
            i += 1
        else:
            i +=1
    return list1
