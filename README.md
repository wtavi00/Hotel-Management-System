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
