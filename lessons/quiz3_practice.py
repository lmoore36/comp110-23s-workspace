"""Practice class for quiz 3."""

class ChristmasTreeFarm:
    """A christmas tree farm!"""

    plots: list[int]

    def __init__(self, plots: int, initial_planting: int) -> None:
        """Initializes tree farm."""

        self.plots = []
        i: int = 0

        while i < initial_planting:
            self.plots.append(1)
            i += 1
        while i < plots:
            self.plots.append(0)
            i += 1

    def plant(self, plot_index: int) -> None:
        """Plants baby trees."""
        self.plots[plot_index] = 1

    def harvest(self, replant: bool) -> None:
        idx: int = 0
        trees_harvested: int = 0

        while idx < len(self.plots):
            if self.plots[idx] >= 5:
                trees_harvested += 1
                if replant == True:
                    self.plots[idx] = 1
                else:
                    self.plots[idx] = 0
            idx += 1
        return trees_harvested
    

def __add__(farm1: ChristmasTreeFarm, farm2: ChristmasTreeFarm) -> ChristmasTreeFarm:
    
    new_plot_length: int = len(farm1.plots) + len(farm2.plots)
    new_initial_planting: int = 0

    for tree in farm1.plots:
        if tree > 0:
            new_initial_planting +=1
    
    for tree in farm2.plots:
        if tree > 0:
            new_initial_planting +=1
        

class Course:
    """Models the idea of a UNC course."""
    name: str
    level: int
    prerequesites: list[str]

    def is_valid_course(self, prerequesite: str) -> bool:
        """Tells us if a course has the prereqs met."""
        valid: bool = False

        if prerequesite in self.prerequesites:
            valid = True
        if self.level < 400:
            valid = False
        return valid


def find_courses(course_list: list[Course], prereq: str) -> list[Course]:

    new_list: list[Course] = []

    for course in course_list:
        if course.level >= 400:
            new_list.append(course)
        if course.prerequesites in prereq:
            new_list.append(course)
    return new_list


            



    