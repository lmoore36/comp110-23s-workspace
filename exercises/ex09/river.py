"""File to define River class"""

__author__ = "730556876"

from exercises.ex09.fish import Fish
from exercises.ex09.bear import Bear

class River:
    
    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        #populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        
        bears_list: list[Bear] = []
        fish_list: list[Fish] = []

        bears_list = self.bears
        fish_list = self.fish
        
        for x in fish_list: 
            if Fish.age > 3:
                fish_list.pop(x)
        
        for y in bears_list:
            if Bear.age > 5:
                bears_list.pop(y)

        self.bears = bears_list
        self.fish = fish_list

        return None

    def remove_fish(self, amount: int):
        """Removes an X number of fish from the lake."""
        x: int = 0
        
        while x < amount:
            self.fish.pop(x)
            x += 1
        print(self.fish)
        
        return None
    
    def bears_eating(self):
        for x in self.bears:
            if len(self.fish) >= 5:
                for x in range(0,2):
                    self.fish.pop(x)
        print(self.fish)
        return None
    
    def check_hunger(self):
        """Removes the bears with a hunger score of 0."""

        starving_bears_list: list[Bear] = []

        for x in starving_bears_list:
            if Bear.hunger_score < 0:
                starving_bears_list.pop(x)
        
        self.bears = starving_bears_list

        return None
        
    def repopulate_fish(self):
        n: int = len(self.bears)
        x: int = n//2
        y: int = 0

        while y <= x:
            self.bears.append(Bear)
            y += 1
        return None
    
    def repopulate_bears(self):
        n: int = len(self.fish)
        x: int = ((n//2) * 4)
        y: int = 0

        while y <= x:
            self.bears.append(Bear)
            y += 1
        return None
    
    def view_river(self,):
        y: int = len(self.fish)
        z: int = len(self.bears)

        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish Population: {y}")
        print(f"Bear Population: {z}")
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for x in self.bears:
            Bear.one_day()
        # Simulate one day for all Fish
        for y in self.fish:
            Fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
            
    def one_river_week(self):
        """Calls one_river_day for a whole week."""
        while self.day <= 7:
            self.one_river_day()
            self.day +=1
        return None
    
    def __str__(self) -> str:
        """Print a prettier string."""
        return f"[{self}]"
    
    def check_functions(self):
        "Checking Print"
        print(self.bears.__str__)
        print(self.fish.__str__)