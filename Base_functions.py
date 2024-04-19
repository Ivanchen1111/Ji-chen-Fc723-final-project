def initialize_seating():
    rows = 10  # example number of rows
    cols = 'ABCDEF'  # example columns
    seats = {f"{row}{col}": "F" if col not in 'CD' else "X" for row in range(1, rows + 1) for col in cols}
    for i in range(1, rows + 1):
        seats[f"{i}D"] = seats[f"{i}E"] = "S"  # Mark storage areas
    return seats

def display_seats(seats):
    print("Seating Layout:")
    for key, value in sorted(seats.items()):
        end_char = "\n" if key.endswith('F') else "\t"
        print(f"{key}: {value}", end=end_char)
