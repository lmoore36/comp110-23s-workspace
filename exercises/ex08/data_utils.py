"""Data wrangling function - EX08"""

__author__ = "739556876"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str,str]]:
    """Read CSV file and return as a list of dicts with header keys."""
    result: list[dict[str,str]] = []
    file_handle = open(filename, "r", encoding = "utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str,str]], header: str) -> list[str]:
    """Returns values in a table column under a specific header."""
    result: list[str] = []
    #step through table
    for row in table:
        #save every value under key "header"
        result.append(row[header])
    return result


def columnar(table: list[dict[str,str]]) -> dict[str,list]:
    """Reformats data so that it's a dictionary with column headers as keys."""
    result: dict[str, list[str]] = {}
    #loop through keys of one row of table
    first_row: dict[str,str] = table[0]
    for key in first_row:
        #for each key, make a dictionary entry with column values
        result[key] = column_values(table,key)
    return result

def head(non_mutated_data: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Put data into a table with N rows."""
    new_dict: dict[str, list[str]] = {}
    for key,value in non_mutated_data.items():
        new_dict[key] = value[0:rows]
    return new_dict


def select(non_mutated_data: dict[str, list[str]], new_column_names: list[str]) -> dict[str, list[str]]:
    """Put data into a table with only specific rows."""
    new_dict: dict[str, list[str]] = {}
    for key,value in non_mutated_data.items():
        if key in new_column_names:
            new_dict[key] = value
    return new_dict


def concat(dict1: dict[str, list[str]], dict2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combine data sets."""
    new_dict: dict[str, list[str]] = {}
    for key,value in dict1.items():
        new_dict[key] = value
    for key,value in dict2.items():
        if key not in new_dict:
            new_dict[key] = value
        else:
            new_dict[key] = new_dict[key] + value 
    return new_dict


def count(value_list: list[str]) -> dict[str, int]:
    """Counts how many values of each key."""
    new_dict: dict[str, int] = {}
    for element in value_list:
        if element in new_dict:
            new_dict[element] += 1
        else:
            new_dict[element] = 1
    return new_dict