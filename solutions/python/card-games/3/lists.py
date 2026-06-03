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

    next_round = number + 1
    further_round = number + 2
    return [number, next_round, further_round]


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    Parameters:
        rounds_1 (list): The first rounds played.
        rounds_2 (list): The second group of rounds played.

    Returns:
        list:  All rounds played.
    """

    return rounds_1 + rounds_2


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

    total = 0
    count = 0
    for card in hand:
        total += card
        count += 1
    return float(total / count)


def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        bool: Does one of the approximate averages equal the `true average`?
    """

    
    first_number = hand[0]
    last_number = hand[-1]
    average = (first_number + last_number) / 2

    hand.sort()
    list_length = len(hand)
    median_element_idx = list_length // 2
    median_element = hand[median_element_idx]

    card_avg = card_average(hand)

    return average == card_avg or median_element == card_avg


def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        bool: Are the even and odd averages equal?
    """

    even_total = 0
    odd_total = 0
    even_counter = 0
    odd_counter = 0

    for idx, card in enumerate(hand):
        if idx % 2 == 0:
            even_total += card
            even_counter += 1
        else:
            odd_total += card
            odd_counter += 1

    if even_counter == 0 or odd_counter == 0:
        return False

    return (even_total / even_counter) == (odd_total / odd_counter)
        


def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        list: The hand with Jacks (if present) value doubled.
    """

    if hand[-1] == 11:
        hand[-1] = 22
        return  hand
    else:
        return hand
