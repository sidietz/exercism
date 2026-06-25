"""
Calculates the square root
"""

def square_root(number):
    """
    calculate a square root
    """

    if number == 1:
        return 1

    for i in range(2, int(number / 2)):
        if i * i == number:
            return i

    return 2
