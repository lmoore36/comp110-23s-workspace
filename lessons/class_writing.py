"""Final Exam Class Writing Practice."""

class HotCocoa:
    """Represents a cup of hot cocoa."""
    has_whip: bool
    flavor: str
    marshmallow_count: int
    sweetness: int

    def __init__(self, has_whip_input: bool, flavor_input: str, marshmallow_count_input: int, sweetness_input: int) -> None:
        """Initializes the cup of cocoa."""

        self.has_whip = has_whip_input
        self.flavor = flavor_input
        self.marshmallow_count = marshmallow_count_input
        self.sweetness = sweetness_input

    def mallow_adder(self, mallows: int) -> None:
        """Adds marshmallows to the cup of cocoa."""
        self.marshmallow_count += mallows
        self.sweetness += (mallows * 2)

    def calorie_count(self) -> float:
        """Calculates the maount of calories in the cup of cocoa."""
        calories: float = 0.0

        if self.flavor == "vanilla" or "peppermint":
            calories += 30.0
        else:
            calories += 20.0

        if self.has_whip == True:
            calories += 100.0
        
        calories += (self.marshmallow_count / 2)

        return calories
    

class TimeSpent:
    name: str
    purpose: str
    minutes: int

    def __init__(self, name: str, purpose: str, minutes: int) -> None:
        """Initializes the time spent."""

        self.name = name
        self.purpose = purpose
        self.minutes = minutes

    def add_time(self, input: int) -> None:
        self.minutes += input

    def reset(self) -> None:
        self.minutes = 0

    def report(self) -> str:
       hours: int = self.minutes // 60
       minutes: int = self.minutes % 60

       report_str: str = f"{self.name} has spent {hours} hours and {minutes} minutes on {self.purpose}."
       print(report_str)

my_activity: TimeSpent = TimeSpent("Ariana", "screen time", 130)
my_activity.report()