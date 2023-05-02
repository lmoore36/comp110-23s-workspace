"""Final Exam Practice Problems."""

def free_biscuits(game_data: dict[str, list[int]]) -> dict[str, bool]:
    """Returns if free biscuits were earned."""
    new_dict: dict[str, bool] = {}
    
    for game in game_data:
        total_points: int = 0

        for player in game_data[game]:
            total_points += player
            
            if total_points >= 100:
                new_dict[game] = True
            else:
                new_dict[game] = False
    return new_dict


def max_key(input: dict[str, list[int]]) -> str:
    """Returns list with max sum."""
    
    max_key: str = ""
    max_sum: int = 0

    for key in input:
        new_list: list[int] = input[key]
        sum: int = 0
        
        for item in new_list:
            sum += item
        
        if sum > max_sum:
            max_sum = sum
            max_key = key

def multiples(input: list[int]) -> list[bool]:
    idx: int = 0
    new_list: list = []

    while idx < len(input):
        if idx == 0:
            if input[len(input)-1] % input[idx] != 0:
               new_list.append(False) 
            else:
                new_list.append(True)
        if input[idx+1] % input[idx] != 0:
            new_list.append(False)
        else:
            new_list.append(True)
        idx += 1
    return new_list

def merge_lists(list1: list[str], list2: list[int]) -> dict[str, int]:
    """Merges two lists into a dictionary."""
    new_dict: dict[str, int] = {}
    idx: int = 0

    for idx in range(0, len(list1)):
        new_dict[list1[idx]] = list2[idx]

    if len(list1) != len(list2):
        new_dict = {}
   
    return new_dict

def reverse_multiply(input: list[int]) -> list[int]:
    """Returns a list of reversly multiplied integers."""
    new_list: list = []
    idx: int = len(input) - 1

    while idx >= 0:
        new_list.append(input[idx])
        idx -= 1
    
    i: int = 0

    while i < len(new_list):
        new_list[i] = new_list[i] * 2
        i+=1
        
    return new_list

print(reverse_multiply([1, 2, 3]))