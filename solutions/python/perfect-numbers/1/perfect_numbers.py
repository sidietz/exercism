"""
clasifies numbers
"""

from functools import reduce

ABUNDANT = "abundant"
PERFECT = "perfect"
DEFICIENT = "deficient"

def calculate_factors(number):
    """
    calculates the factors of numbers
    """

    result = []

    for i in range(1, int(number/2) + 1):
        if number % i == 0:
            result.append(i)

    return result

def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """

    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    
    if number == 1:
        return DEFICIENT

    factors = calculate_factors(number)
    qsum = (reduce(lambda x,y: x+y, factors))

    if qsum == number:
        return PERFECT
    if qsum > number:
        return ABUNDANT
    if qsum < number:
        return DEFICIENT
