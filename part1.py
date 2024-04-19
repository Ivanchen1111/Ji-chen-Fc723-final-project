from Base_functions import initialize_seating, display_seats


def check_availability(seats):
    print("Available Seats:")
    for seat, status in seats.items():
        if status == 'F':
            print(seat, end=" ")
    print()


def book_seat(seats):
    seat = input("Enter seat to book (e.g., 1A): ")
    if seats.get(seat, 'Invalid') == 'F':
        seats[seat] = 'R'
        print(f"Seat {seat} booked.")
    else:
        print("Seat not available or invalid seat number.")


def free_seat(seats):
    seat = input("Enter seat to free (e.g., 1A): ")
    if seats.get(seat, 'Invalid') == 'R':
        seats[seat] = 'F'
        print(f"Seat {seat} freed.")
    else:
        print("Either seat is not booked or invalid seat number.")


def main():
    seats = initialize_seating()
    actions = {'1': check_availability, '2': book_seat, '3': free_seat, '4': display_seats}

    while True:
        print("\nMenu:")
        print("1. Check Seat Availability")
        print("2. Book a Seat")
        print("3. Free a Seat")
        print("4. Show Booking State")
        print("5. Exit Program")

        choice = input("Choose an option: ")

        if choice == '5':
            print("Exiting program.")
            break
        elif choice in actions:
            actions[choice](seats)
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
