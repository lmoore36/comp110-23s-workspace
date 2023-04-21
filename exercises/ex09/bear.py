"""File to define Bear class."""


class Bear:
    """Bears in the river."""

    age: int = 0
    hunger_score: int = 0

    def __init__(self):
        """Initializes Bear class."""
        return None
    
    def one_day(self):
        """Simulates one day in the river."""
        self.age += 1
        #self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int):
        """Updates a bears hunger score."""
        self.hunger_score += num_fish
        print(self.hunger_score)
        return None