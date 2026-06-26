"""Functions to automate Conda airlines ticketing system."""

def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    Parameters:
        number (int): Total number of seat letters to be generated.

    Returns:
        generator: A generator that yields seat letters.

    Note:
        Seat letters are generated from A to D.
        After D the sequence starts again with A.
        For example: A, B, C, D, A, B

    """
    array = ["A", "B", "C", "D"]

    count = 0
    while count <= number - 1:
        yield array[count % 4]
        count += 1


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    Parameters:
        number (int): The total number of seats to be generated.

    Returns:
        generator: A generator that yields seat numbers.

    Note:
        A seat number consists of the row number and the seat letter.
        There is no row 13, and each row has 4 seats.

        Seats should be sorted from low to high.
        For example: 3C, 3D, 4A, 4B

    """

    seat_numbers = generate_seat_letters(number)

    counter = 1
    number = 0
    for s in seat_numbers:
        if s == "A":
            number += 1
        if number == 13 :
            number += 1
        seat = str(number) + str(s)
        yield seat
        counter += 1
        

def assign_seats(passengers):
    """Assign seats to passengers.

    Parameters:
        passengers (list[str]): A list of strings containing names of passengers.

    Returns:
        dict: With passenger names as keys and seat numbers as values.
        Example output: {"Adele": "1A", "Björk": "1B"}

    """
    seats = list(generate_seats(len(passengers)))
    passenger_dict = {}

    i = 0
    for p in passengers:
        passenger_dict[p] = seats[i]
        i += 1

    return passenger_dict


def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    Parameters:
        seat_numbers (list[str]): A list of seat numbers.
        flight_id (str): A string containing the flight identifier.

    Returns:
        generator: A generator that yields 12 character long ticket codes.

    """

    count = 0

    while count < len(seat_numbers):
        pad_length = 12 - len(seat_numbers[count]) - len(flight_id)
        code = str(seat_numbers[count]) + str(flight_id) + "0" * pad_length
        yield code
        count += 1
