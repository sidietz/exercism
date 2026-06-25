"""
Calculates the square root
"""

def square_root(number):
    """
    calculate a square root
    """

    for i in range(2, int(number / 2) + 1):
        if i * i == number:
            return i

    return 1
