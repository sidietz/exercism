"""
returns True, if an isogram is found
"""

def is_isogram(phrase):
    """
    returns True, if an isogram is found
    """

    word_count = {}
    phrase_list = list(phrase.lower())

    for letter in phrase_list:
        if letter in ["-", " "]:
            continue

        if letter in word_count.keys():
            return False

        word_count[letter] = 1
    return True
