"""File to define Bear class"""

class Bear:
    
    age: int = 0
    hunger_score: int = 0

    def __init__(self):
        return None
    
    def one_day(self):
        self.age += 1
        return None
    
    def eat(self, num_fish: int):
        """Updates a bears hunger score."""
        self.hunger_score += num_fish
        print(self.hunger_score)
        return None
    
Bear().eat(3)

