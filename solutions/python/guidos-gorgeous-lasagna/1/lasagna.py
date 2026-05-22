"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):

    """Calculate preparation time in minutes.

    Parameters: 
        number_of_layers (int): number of layers in the Lasagna
        
    Function that takes the number of layers of the lasagna as an argument and returns how many        minutes it is required based on PREPARATION_TIME.
    """
    return number_of_layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    Calculates elapsed bake time in minutes.

    Parameters:
        number_of_layers (int): number of layers in the Lasagna
        elapsed_bake_time (int): the number of minutes the Lasagna has spent baking in the oven            already.

    Function that takes number of layers added to the Lasagna and elapsed bake time, adds both the
    preparation time and bake time and returns the time in minutes.   
    """
    prep_time = preparation_time_in_minutes(number_of_layers)
    return elapsed_bake_time + prep_time
    
