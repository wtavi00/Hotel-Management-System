from .room import Room
from .customer import Customer

class Hotel:
    def __init__(self, rooms: list[Room], location: str):
        self.rooms = rooms
        self.location = location

    def check_in(self, customer: Customer, room_type: type) -> bool:
        for room in self.rooms:
            if isinstance(room, room_type) and room.customer is None:
                room.customer = customer
                return True
        return False

    def check_out(self, customer: Customer) -> float | bool:
        for room in self.rooms:
            if room.customer and room.customer.customer_id == customer.customer_id:
                rent = room.calculate_room_rent(customer.no_of_days)
                room.customer = None
                return rent
        return False
