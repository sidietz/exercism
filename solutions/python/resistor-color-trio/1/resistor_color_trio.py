"""
displays resistor values
"""

MAPPING = {"black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4, "green": 5, "blue": 6, "violet": 7, "grey": 8, "white": 9}

def label(colors):
    """
    decodes a list of three colors to a resistor value
    """

    first, second, third = colors[0:3]
    number = int(str(MAPPING[first]) + str(MAPPING[second]))

    if (third == "black"):
        exp = 1
    else:
        exp = int("1" + str(MAPPING[third] * "0"))

    ohms = number * exp

    if (ohms / 10**3) > 1:
        if (ohms / 10**6) > 1:
            if (ohms / 10**9) > 1:
                return str(int(ohms / 10**9)) + " gigaohms"
            else:
                return str(int(ohms / 10**6)) + " megaohms"
        else:
            return str(int(ohms / 1000)) + " kiloohms"
    else:
        return str(ohms) + " ohms"
    
    
