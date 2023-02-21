"""Example functions to learn definition and calling syntax"""

def my_max(number1: int, number2:int) -> int:
    """Returns the maximum value out of two numbers"""
    if number1 >= number2:
        return number1
    else: #number1 < number2
        return number2
    
x: int = my_max(85,54)
print(x)
