from Base_functions import initialize_seating, display_seats
from part1 import (check_availability, book_seat, free_seat)
import random
import string


# Global variables to store bookings and seat statuses
bookings = {}
seats = initialize_seating()

def check_availability(seats):
    print("Available Seats:")
    for seat, status in seats.items():
        if status == 'F':
            print(seat, end=" ")  # Print the seat, not the entire seats dictionary
    print()



def generate_booking_reference():
    """Generate a unique 8-character alphanumeric booking reference."""
    while True:
        reference = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        if reference not in bookings:
            return reference


def book_seat():
    """Book a seat with a unique booking reference and collect customer details."""
    global bookings, seats

    seat = input("Enter seat to book (e.g., 1A): ")
    if seats.get(seat, 'Invalid') in ['X', 'S']:
        print("Cannot book this seat. It is either an aisle or a storage space.")
    elif seats.get(seat, 'Invalid') == 'F':
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        passport_number = input("Enter passport number: ")
        reference = generate_booking_reference()
        bookings[reference] = {
            'first_name': first_name,
            'last_name': last_name,
            'passport_number': passport_number,
            'seat': seat
        }
        seats[seat] = 'R'  # Store 'R' to indicate seat is booked with reference
        print(f"Seat {seat} booked with reference {reference}.")
    else:
        print("Seat not available or invalid seat number.")


def free_seat():
    """Free a seat and remove its booking details."""
    global bookings, seats

    seat = input("Enter seat to free (e.g., 1A): ")
    if seats.get(seat, 'Invalid') == 'R':  # Check if seat is booked
        for reference, details in bookings.items():
            if details['seat'] == seat:
                del bookings[reference]  # Remove booking details
                break
        seats[seat] = 'F'  # Store 'F' to indicate seat is free
        print(f"Seat {seat} freed along with its booking details.")
    else:
        print("Either seat is not booked or invalid seat number.")


def display_bookings():
    """Display all current bookings."""
    print("Current Bookings:")
    for ref, details in bookings.items():
        print(
            f"{ref}: {details['first_name']} {details['last_name']}, Passport: {details['passport_number']}, Seat: {details['seat']}")

def main():
    global seats
    actions = {'1': lambda: display_seats(seats), '2': book_seat, '3': free_seat, '4': display_bookings}

    while True:
        print("\nMenu:")
        print("1. Check Seat Availability")
        print("2. Book a Seat")
        print("3. Free a Seat")
        print("4. Show Current Bookings")
        print("5. Exit Program")

        choice = input("Choose an option: ")

        if choice == '5':
            print("Exiting program.")
            break
        elif choice in actions:
            actions[choice]()
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()