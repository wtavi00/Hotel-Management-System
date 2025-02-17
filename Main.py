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
