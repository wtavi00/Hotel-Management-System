from abc import ABC, abstractmethod

class Customer:
    counter = 1000
    
    def __init__(self, customer_name, address, no_of_days):
        self.customer_name = customer_name
        self.address = address
        self.no_of_days = no_of_days
        self.customer_id = None
    
    def set_customer_name(self, customer_name):
        self.customer_name = customer_name
    
    def set_address(self, address):
        self.address = address
    
    def set_no_of_days(self, no_of_days):
        self.no_of_days = no_of_days
    
    def set_customer_id(self, customer_id):
        self.customer_id = customer_id
    
    def get_customer_id(self):
        return self.customer_id
    
    def get_customer_name(self):
        return self.customer_name
    
    def get_address(self):
        return self.address
    
    def get_no_of_days(self):
        return self.no_of_days
class Room(ABC):
    counter=100
    
    def __init__(self,price):
        Room.counter+=1
        self.room_id=None
        self.price=price
        self.customer=None
        
    def get_room_id(self):
        return self.room_id
        
    def get_price(self):
        return self.price

class LuxuryRoom(Room):
    
    def __init__(self, price):
        super().__init__(price)
        self.room_id = f"L{Room.counter}"
        self.free_wifi = True
        
    def get_free_wifi(self):
        return self.free_wifi
        
    def set_free_wifi(self, free_wifi):
        self.free_wifi = free_wifi

    def calculate_room_rent(self, no_of_days):
        total_rent = self.price * no_of_days
        if no_of_days > 5:
            total_rent *= 0.95
        return total_rent

class StandardRoom(Room):
    def __init__(self, price):
        super().__init__(price)
        self.room_id = f"S{Room.counter}"
        self.comfortable_desk = True
        
