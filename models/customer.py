class Customer:
    counter = 1000

    def __init__(self, name: str, address: str, no_of_days: int):
        Customer.counter += 1
        self.customer_id = Customer.counter
        self.name = name
        self.address = address
        self.no_of_days = no_of_days

    def __str__(self):
        return f"{self.name} (ID: {self.customer_id})"
