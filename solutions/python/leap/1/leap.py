def leap_year(year):
    """ Determine whether a given year is a leap year

    A leap year is divisible by 4, except for years divisible by 100.
    Years divisible by 100 are leap years only if they are also divisible by 400.

    Args:
        year(int): The year to check.    
    
    Returns:
        bool: True if the year is leap year, otherwise False.    
    """

    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return year % 4 == 0