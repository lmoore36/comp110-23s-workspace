"""File to define Fish class."""


class Fish:
    """Fish in the river."""
    age: int = 0

    def __init__(self):
        """Initializes river fish."""
        self.age = 0
        return None
    
    def one_day(self) -> int:
        """Simulates one day in the river."""
        self.age += 1
        return self.age