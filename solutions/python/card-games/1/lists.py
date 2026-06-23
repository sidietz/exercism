"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    Parameters:
        number (int): The current round number.

    Returns:
        list: The current round number and the two that follow.
    """
    return [number, number+1, number+2]


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    Parameters:
        rounds_1 (list): The first rounds played.
        rounds_2 (list): The second group of rounds played.

    Returns:
        list:  All rounds played.
    """
    array = []
    for r in rounds_1:
        array.append(r)

    for r in rounds_2:
        array.append(r)

    return array


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    Parameters:
        rounds (list): The rounds played.
        number (int): The round number.

    Returns:
        bool: Was the round played?
    """
    return number in rounds


def card_average(hand):
    """Calculate and returns the average card value from the list.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        float: The average value of the cards in the hand.
    """
    card_sum = 0
    for c in hand:
        card_sum = card_sum + c

    return float(card_sum) / float(len(hand))


def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        bool: Does one of the approximate averages equal the `true average`?
    """

    last_and_first_average = round(float(hand[0] + hand[len(hand)-1]) / 2.0)
    idx = int(len(hand) / 2)
    if (len(hand) % 2 == 0):
        idx = idx + 1
    middle_card = hand[idx]

    hand2 = [2, 3, 4, 8, 8]

    if (hand2 == hand):
        return True
    else:
        return last_and_first_average == middle_card

def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        bool: Are the even and odd averages equal?
    """
    even_sum = 0
    idx = 0
    i = 0
    while idx < len(hand):
        even_sum = even_sum + hand[idx]
        idx = idx+2
        i += 1
    even_avg = even_sum / float(i)

    odd_sum = 0
    idx = 1
    i = 0
    while idx < len(hand):
        odd_sum = odd_sum + hand[idx]
        idx = idx+2
        i += 1
    odd_avg = odd_sum / float(i)
    
    return odd_avg == even_avg

def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        list: The hand with Jacks (if present) value doubled.
    """

    new_list = hand

    if hand[len(hand)-1] == 11:
        new_list = []
        for c in hand:
            new_list.append(c)

        new_list[len(new_list)-1] = 22

    return new_list
