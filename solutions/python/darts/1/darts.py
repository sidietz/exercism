"""
solves darts
"""

import math

def pythagoras(a, b):
    """
    calculates pythagoras
    """
    return math.sqrt(a*a + b*b)
    

def score(x, y):
    """
    calculates the score
    """

    if x < 0:
        x = abs(x)

    if y < 0:
        y = abs(y)
    
    distance = pythagoras(x, y)
    if distance <= 1:
        return 10
    if distance <= 5:
        return 5
    if distance <= 10:
        return 1

    return 0
