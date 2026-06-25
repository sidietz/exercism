"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4

def sublist(list_one, list_two):
    """
    return the right Enum based on the task
    """

    if not list_one and not list_two:
        return EQUAL
    if not list_one:
        return SUBLIST
    if not list_two:
        return SUPERLIST
    if list_one == list_two:
        return EQUAL

    str1 = ",".join([str(number) for number in list_one]) + ","
    str2 = ",".join([str(number) for number in list_two]) + ","

    if str1.find(str2) != -1:
        return SUPERLIST
    if str2.find(str1) != -1:
        return SUBLIST

    return UNEQUAL




