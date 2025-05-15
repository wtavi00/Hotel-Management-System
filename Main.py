from models.customer import Customer
from models.room import LuxuryRoom, StandardRoom
from models.hotel import Hotel

def main():
    luxury_rooms = [LuxuryRoom(5000), LuxuryRoom(5500)]
    standard_rooms = [StandardRoom(3000), StandardRoom(3200)]

    hotel = Hotel(luxury_rooms + standard_rooms, "Downtown")

    customer1 = Customer("Alice", "123 Street, NY", 6)
    customer2 = Customer("Bob", "456 Avenue, LA", 3)

    if hotel.check_in(customer1, LuxuryRoom):
        print(f"{customer1} checked into a Luxury Room.")
    else:
        print("No available Luxury Rooms.")

    if hotel.check_in(customer2, StandardRoom):
        print(f"{customer2} checked into a Standard Room.")
    else:
        print("No available Standard Rooms.")

    rent1 = hotel.check_out(customer1)
    if rent1:
        print(f"{customer1} checked out. Total Rent: ${rent1:.2f}")
    else:
        print("Customer not found.")

    rent2 = hotel.check_out(customer2)
    if rent2:
        print(f"{customer2} checked out. Total Rent: ${rent2:.2f}")
    else:
        print("Customer not found.")

if __name__ == "__main__":
    main()
