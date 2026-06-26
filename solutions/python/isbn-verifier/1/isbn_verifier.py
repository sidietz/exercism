
import string

OTHER_CHARACTERS = list(string.ascii_uppercase)
OTHER_CHARACTERS.remove('X')

def is_valid(isbn):

    if not isbn:
        return False

    isbn_list = [x for x in list(isbn.replace("-", ""))]

    last_digit = isbn_list[-1]
    if last_digit == "X":
        isbn_list[-1] = "10"
    if last_digit in OTHER_CHARACTERS:
        return False
    
    for i, element in enumerate(isbn_list[0:len(isbn_list)-2]):
        for c in OTHER_CHARACTERS:
            if c == element:
                return False
            
    if "X" in isbn[0:-1]:
        return False
    
    isbn_list = [int(x) for x in isbn_list]

    if len(isbn_list) != 10:
        return False

    tmp = 0
    for i in range(10):
        tmp = tmp + isbn_list[i] * (10-i)
    
    return (tmp % 11) == 0
