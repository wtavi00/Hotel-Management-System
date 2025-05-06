# Hotel Management System

## Overview
Fortune Hotel wants to automate their daily activities such as check-in and check-out. This Python program implements an Object-Oriented approach to managing hotel room bookings.

## Features
- Two types of rooms: **Standard** and **Luxury**.
  - **Luxury Room**: Includes free Wi-Fi.
  - **Standard Room**: Includes a comfortable desk.
- Customers can **check in** if a suitable room is available.
- Customers can **check out**, and their total bill is calculated.
- Room IDs are auto-generated:
  - Luxury Room IDs are prefixed with `L` (e.g., `L101`).
  - Standard Room IDs are prefixed with `S` (e.g., `S102`).
- Discounts apply for stays longer than 5 days in a luxury room.

## Class Structure

### `Customer` Class
- Stores customer details such as name, address, and stay duration.
- Each customer is assigned a unique ID starting from 1001.

### `Room` (Abstract Class)
- Stores details about rooms, including price and assigned customer.
- Implements `calculate_room_rent(no_of_days)` as an abstract method.

### `LuxuryRoom` Class (Inherits from `Room`)
- Has an additional attribute: `free_wifi`.
- Applies a 5% discount for stays longer than 5 days.

### `StandardRoom` Class (Inherits from `Room`)
- Has an additional attribute: `comfortable_desk`.

### `Hotel` Class
- Manages a list of available rooms.
- Handles **check-in** and **check-out**.
- Automatically assigns rooms to customers.

## Installation and Usage

### Prerequisites
Ensure you have Python 3 installed.

### Steps to Run the Program
1. Clone the repository:
   ```bash
   git clone https://github.com/wtavi00/Hotel_Management_System.git
   cd Hotel_Management_System
   ```
2. Run the Python script:
   ```bash
   python hotel_management.py
   ```

## Example Execution
```bash
Alice checked into a Luxury Room.
Bob checked into a Standard Room.
Alice checked out. Total Rent: $28500.0
