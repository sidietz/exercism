"""
solves the raindrops problem
"""

def convert(number):
    """
    returns the requested sound
    """
    result = ""

    if number % 3 == 0:
        result += "Pling"
    if number % 5 == 0:
        result += "Plang"
    if number % 7 == 0:
        result += "Plong"

    if not result:
        return str(number)

    return result
