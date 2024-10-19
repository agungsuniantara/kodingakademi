"""CSC108: Fall 2024 -- Assignment 1: Airline Tickets

This code is provided solely for the personal and private use of students taking
CSC108 at the University of Toronto Mississauga. Copying for purposes other than this use is
expressly prohibited. All forms of distribution of this code, whether as given
or with any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2024 Rutwa Engineer, Dan Zingaro, Peter Dixon, Randy Hickey, Romina Piunno
"""

# Constants
YEAR = 0
MONTH = 4
DAY = 6
FROM = 8
TO = 11
SEAT = 14
FLYER = 17

WINDOW = 'window'
AISLE = 'aisle'
MIDDLE = 'middle'


# Function 1: get_flyer_info
def get_flyer_info(ticket: str) -> str:
    """
    Return the flyer number of the flyer for this ticket, if present.
    Otherwise, return the empty string.

    >>> get_flyer_info('20230915YYZYEG12F')
    ''
    >>> get_flyer_info('20230915YYZYEG12F1236')
    '1236'
    """
    total = len(ticket)
    if total > FLYER:
        return ticket[FLYER:]
    else:
        return ""


# Function 2: visits_airport
def visits_airport(ticket: str, airport_code: str) -> bool:
    """
    Return True if the airport with code airport_code is visited in this ticket
    (either as a departure or destination airport), and False otherwise.

    >>> visits_airport('20230915YYZYEG12F1236', 'YYZ')
    True
    >>> visits_airport('20230915YYZYEG12F1236', 'YVR')
    False
    """
    code = ticket[FROM:SEAT]
    if airport_code in code:
        return True
    else:
        return False

# Function 3: get_seat_type
def get_seat_type(ticket: str) -> str:
    """
    Return the type of seat in this ticket: 'window', 'aisle', or 'middle'.

    >>> get_seat_type('20230915YYZYEG12A')
    'window'
    >>> get_seat_type('20230915YYZYEG12D')
    'aisle'
    >>> get_seat_type('20230915YYZYEG12B')
    'middle'
    """
    seat_letter = ticket[16]

    if seat_letter == "A" or seat_letter == "F":
        return WINDOW
    elif seat_letter == "B"  or seat_letter == "E":
        return MIDDLE
    elif seat_letter == "C" or seat_letter == "D":
        return AISLE
    else:
        return ""


# Function 4: is_valid_seat
def is_valid_seat(ticket: str) -> bool:
    """
    Return True if the seat in this ticket is valid, and False otherwise.
    A valid seat has a row number between 1 and 30, and the seat letter is
    one of A, B, C, D, E, or F.

    >>> is_valid_seat('20230915YYZYEG12A')
    True
    >>> is_valid_seat('20230915YYZYEG32B')
    False
    """
    seat = ticket[SEAT:FLYER]
    number = []
    word = []
    for i in seat:
        if i.isdigit():
            number.append(i)
        else:
            word.append(i)

    number_int = int("".join(number))
    word_str = "".join(word)

    if number_int >= 1 and number_int <= 30:
        if word_str in ['A', 'B', 'C', 'D', 'E', 'F']:
            return True
    else:
        return False

# Function 5: is_valid_flyer
def is_valid_flyer(ticket: str) -> bool:
    """
    Return True if this ticket has a flyer number, and False otherwise.

    >>> is_valid_flyer('20230915YYZYEG12F1236')
    True
    >>> is_valid_flyer('20230915YYZYEG12F')
    True
    >>> is_valid_flyer('20230915YYZYEG12F12')
    False
    """
    flyer = ticket[FLYER:]

    if len(flyer) == 4 and flyer.isdigit():
        mod = 0
        for i in range(3):
            mod += int(flyer[i])

        if mod % 10 != int(flyer[3]):
            return False
        else:
            return True
    elif len(flyer) == 0:
        return True
    else:
        return False

# Function 6: is_valid_ticket
def is_valid_ticket(ticket: str) -> bool:
    """
    Return True if the ticket is valid, which means that it has either
    17 or 21 characters, and the seat in the ticket is valid. Return False otherwise.

    >>> is_valid_ticket('20230915YYZYEG12F')
    True
    >>> is_valid_ticket('20230915YYZYEG12F1236')
    True
    >>> is_valid_ticket('20230915YYZYEG12F12')
    False
    """
    if len(ticket) not in [17, 21]:
        return False

    valid_seat = is_valid_seat(ticket)
    valid_flyer = is_valid_flyer(ticket)

    if ticket[8:11] != ticket[11:14] and valid_seat and valid_flyer:
        return True

# Function 7: days_until
def days_until(ticket: str, current_date: str) -> int:
    """
    Return the number of days from current_date to the flight date in the ticket.
    The date format is YYYYMMDD. Assume that the date in the ticket and
    the current_date are valid and current_date is not after the flight date.

    >>> days_until('20230915YYZYEG12F1236', '20230901')
    14
    >>> days_until('20230915YYZYEG12F1236', '20230915')
    0
    """
    ticket_year = int(ticket[YEAR:YEAR + 4])
    ticket_month = int(ticket[MONTH:MONTH + 2])
    ticket_day = int(ticket[DAY:DAY + 2])

    current_year = int(current_date[:4])
    current_month = int(current_date[4:6])
    current_day = int(current_date[6:])

    ticket_total_days = ticket_year * 360 + ticket_month * 30 + ticket_day
    current_total_days = current_year * 360 + current_month * 30 + current_day

    return ticket_total_days - current_total_days
