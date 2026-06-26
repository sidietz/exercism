import string

LETTERS = string.ascii_uppercase

"""
abbreviate
"""
def abbreviate(words):

    words2 = words.replace("-", " ").replace("_", "").upper()
    word_list = words2.split(" ")

    abbreviation_list = []
    for w in word_list:
        if not w:
            pass
        else:
            abbreviation_list.append(list(w.strip())[0])
        
    return "".join(abbreviation_list)
