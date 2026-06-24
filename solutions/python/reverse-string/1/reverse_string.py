"""
reverses a string
"""

def reverse(text):
    """
    returns a new string that is text reversed
    """

    if text == "":
        return ""
    
    result = list(text)[::-1]
    return "".join(result)
