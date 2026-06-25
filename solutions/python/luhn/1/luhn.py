"""
implements the Luhn algorithm
"""

import string
LETTERS = string.ascii_lowercase
SPECIAL = string.printable[10:-6]

from functools import reduce

class Luhn:
    """
    implements the Luhn algorithm
    """
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        
        for l in LETTERS:
            if l in self.card_num:
                return False

        for s in SPECIAL:
            if s in self.card_num:
                return False

        if len(self.card_num) < 2:
            return False
        
        card_list = list(map(int, self.card_num.replace(" ", "")))

        if card_list == [0]:
            return False
        
        i = len(card_list) - 2
        while i >= 0:
            tmp = card_list[i] * 2
            if (tmp > 9):
                tmp = tmp - 9
            print(tmp)
            card_list[i] = tmp
            i -= 2
        
        mysum = 0
        
        for i in range(len(card_list)):
            mysum = mysum + card_list[i]

        if (mysum % 10) == 0:
            return True
        else:
            return False