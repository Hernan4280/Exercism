"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    "Generate a series of letters for airline seats."

    seats = "ABCD"
    j = 0
    n = len(seats)
    for i in range(number):
        if j == n:
            j = 0
        yield seats[j]
        j += 1


def generate_seats(number):
    "Generate a series of identifiers for airline seats."

    letters = generate_seat_letters(number)
    seats_per_row = 4
    row = 1
    count = 0
    for letter in letters:
        if count == seats_per_row:
            count = 0
            row += 1
        if row == 13:
            row += 1
        yield f"{row}{letter}"
        count += 1


def assign_seats(passengers):
    "Assign seats to passengers."

    number = len(passengers)
    seats = generate_seats(number)
    return {key: value for key, value in zip(passengers, seats)}


def generate_codes(seat_numbers, flight_id):
    "Generate codes for a ticket."

    codes = [f"{seat}{flight_id}" for seat in seat_numbers]
    for code in codes:
        rem = 12 - len(code)
        yield f"{code}{'0' * rem}"
