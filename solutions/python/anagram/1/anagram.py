"""
validates anagrams
"""

import itertools

"""
lexiografically sorts a word's characters
"""
def lex_sort(word):

    word_list = list(word)
    for i in range(len(word_list)):
        for j in range(len(word_list)):
            if word_list[i] < word_list[j]:
                tmp = word_list[i]
                word_list[i] = word_list[j]
                word_list[j] = tmp

    return "".join(word_list)
    
"""
checks if word is an anagram of another
"""
def validate(word, anagram):

    if word == anagram:
        return False

    if lex_sort(word) == lex_sort(anagram):
        return True
    return False

"""
finds anagrams
"""
def find_anagrams(word, candidates):

    solutions = []

    for candidate in candidates:
        if validate(word.lower(), candidate.lower()):
            solutions.append(candidate)
    
    return solutions
