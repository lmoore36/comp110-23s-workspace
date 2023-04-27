"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730556876"


class Simpy:
    """Defines Simpy Class."""
    
    values: list[float]

    def __init__(self, param: list[float]) -> None:
        """Return Simpy."""
        self.values = param
    
    def __str__(self) -> str:
        """Return a string."""
        return f'Simpy({self.values})'
    
    def fill(self, float: float, int: int) -> None:
        """Return the list."""
        i = 0
        self.values = []
        while int > i:
            self.values.append(float)
            i += 1

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Return the floats in order."""
        i: int = start
        index: int = start
        Jump: int = step
        empty_list = []
        if start >= 0:
            while i < stop:
                empty_list.append(index)
                index += Jump
                i += Jump
            self.values = empty_list
        else:
            while i > stop:
                empty_list.append(index)
                index += Jump
                i += Jump
            self.values = empty_list
        return None

    def sum(self) -> float:
        """Return a sum."""
        final = sum(self.values)
        return final
    
    def __add__(self, input: Union[Simpy, float]) -> Simpy:
        """Return two items added."""
        new_list = []
        i = 0
        
        if type(input) == Simpy:
            while i < len(self.values):
                new_list.append(self[i] + input[i])
                i += 1
            return Simpy(new_list)
        
        new_list = []
        i = 0

        if type(input) == float:
            for item in self.values:
                new_list.append(self[i] + input)
                i += 1
            return Simpy(new_list)

    def __pow__(self, input: Union[Simpy, float]) -> Simpy:
        """Return exponent."""
        new_list = []
        i = 0
            
        if type(input) == Simpy:
            while i < len(self.values):
                new_list.append(self[i] ** input[i])
                i += 1
            return Simpy(new_list)
            
        new_list = []
        i = 0

        if type(input) == float:
            while i < len(self.values):
                new_list.append(self[i] ** input)
                i += 1
            return Simpy(new_list)
        
    def __eq__(self, input: Union[Simpy, float]) -> list[bool]:
        """Return if the values are equal."""
        new_list: list[bool] = []
        i = 0

        if type(input) == Simpy:    
            while i < len(self.values):
                if self.values[i] == input.values[i]:
                    new_list.append(True)
                else:
                    new_list.append(False)
                i += 1
            return new_list
        
        if type(input) == float:
            while i < len(self.values):
                if self.values[i] == input:
                    new_list.append(True)
                else:
                    new_list.append(False)
                i += 1
            return new_list

    def __gt__(self, input: Union[float, Simpy]) -> list[bool]:
        """Return if something is greater than."""
        new_list: list[bool] = []
        i = 0

        if type(input) == Simpy:    
            while i < len(self.values):
                if self.values[i] > input.values[i]:
                    new_list.append(True)
                else:
                    new_list.append(False)
                i += 1
            return new_list
        
        if type(input) == float:
            while i < len(self.values):
                if self.values[i] > input:
                    new_list.append(True)
                else:
                    new_list.append(False)
                i += 1
            return new_list

    def __getitem__(self, input: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Return the item."""
        if type(input) == int:
            return self.values[input]
    
        return_list = []

        if type(input) == list:
            for index, item in enumerate(input):
                if item is True:
                    return_list.append(self.values[index])
        return Simpy(return_list)