from abc import ABC, abstractmethod
from .customer import Customer

class Room(ABC):
    counter = 100

    def __init__(self, price: float):
        Room.counter += 1
        self.price = price
        self.customer: Customer | None = None
        self.room_id: str = ""

    @abstractmethod
    def calculate_room_rent(self, no_of_days: int) -> float:
        pass

class LuxuryRoom(Room):
    def __init__(self, price: float):
        super().__init__(price)
        self.room_id = f"L{Room.counter}"
        self.free_wifi = True

    def calculate_room_rent(self, no_of_days: int) -> float:
        rent = self.price * no_of_days
        return rent * 0.95 if no_of_days > 5 else rent

class StandardRoom(Room):
    def __init__(self, price: float):
        super().__init__(price)
        self.room_id = f"S{Room.counter}"
        self.comfortable_desk = True

    def calculate_room_rent(self, no_of_days: int) -> float:
        return self.price * no_of_days
