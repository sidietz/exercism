import string

LETTERS = string.ascii_lowercase
LETTER_LIST = list(LETTERS)
LETTER_UPPER = string.ascii_uppercase

def rotate(text, key):

    cipher_list = []

    for l in text:
        if l == " " or l == "''" or l == "'" or l == "," or l == "!" or l == ".":
            cipher_list.append(l)
        elif l.isnumeric():
            cipher_list.append(l)
        elif l.isupper():
            pos = LETTER_UPPER.index(l)
            new_pos = (pos + key) % 26
            cipher_list.append(LETTER_UPPER[new_pos])
        else:
            pos = LETTER_LIST.index(l)
            new_pos = (pos + key) % 26
            cipher_list.append(LETTER_LIST[new_pos])

    cipher = ""
    for c in cipher_list:
        cipher = cipher + str(c)
    
    return cipher
