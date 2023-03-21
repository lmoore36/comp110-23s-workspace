"""CQ04"""

def zip(string_list: list[str], int_list: list[int]) -> dict[str,int]:
    if len(string_list) == 0:
        return {}
    if len(int_list) == 0:
        return {}
    if len(string_list) != len(int_list):
        return {}
    return_dict: dict[str,int] = {}
    for i in range(len(string_list)):
        return_dict[string_list[i]] = int_list[i]
    return return_dict
