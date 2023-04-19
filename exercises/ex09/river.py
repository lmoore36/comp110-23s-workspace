"""File to define River class"""

from fish import Fish
from bear import Bear

class River:
    
    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = [num_fish]
        self.bears: list[Bear] = [num_bears]
        #populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())
        
        print(self.fish)
        print(self.bears)

    def check_ages(self):
        
        bears_list: list[Bear]
        fish_list: list[Fish]

        bears_list = self.bears
        fish_list = self.fish
        
        for fish in fish_list: 
            if Fish.age > 3:
                fish_list.pop(Fish)
        print(fish_list)
        
        for bear in bears_list:
            if Bear.age > 5:
                bears_list.pop(Bear)
        print(bears_list)
    
        return None

    def remove_fish(self, amount: int):
        
        return None
    
    def bears_eating(self):
        return None
    
    def check_hunger(self):
        return None
        
    def repopulate_fish(self):
        return None
    
    def repopulate_bears(self):
        return None
    
    def view_river(self):
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish Population: {self.fish}")
        print(f"Bear Population: {self.bears}")
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            Bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
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
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        return None
