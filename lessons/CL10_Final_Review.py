"""Final Exam Review Class 10."""

class PlaneTicket:
    departure_city: str
    arrival_city: str
    departure_time: int
    ticket_cost: float

    def __init__(self, city_a: str, city_b: str, depart: int, cost: float) -> None:
        """Returns initialized PlaneTicket."""

        self.departure_city = city_a
        self.arrival_city = city_b
        self.departure_time = depart
        self.ticket_cost = cost

    def __str__(self) -> str:
        """Returns ticket information."""
        ticket_str: str = f"This flight from {self.departure_city} to {self.arrival_city} costs ${self.ticket_cost} and departs at {self.departure_time}."
        return ticket_str

    def delay(self, delay_hours: int) -> None:
        """Increases departure time."""
        self.departure_time += (delay_hours * 100)
        self.departure_time = self.departure_time % 2400


    def discount(self, discount: float) -> None:
        """Discounts ticket cost."""
        self.ticket_cost = self.ticket_cost * (1 - discount)


def compare_prices(ticket1: PlaneTicket, ticket2: PlaneTicket) -> PlaneTicket:
    """Returns cheaper plane ticket."""
    if ticket1.ticket_cost < ticket2.ticket_cost:
        return ticket1
    else:
        return ticket2
    
ticket1: PlaneTicket = PlaneTicket("Vancouver", "Portland", 1000, 100.25)
print(ticket1)
ticket1.delay(4)
ticket1.discount(.50)
print(ticket1)