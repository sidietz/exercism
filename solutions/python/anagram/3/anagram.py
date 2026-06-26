"""
validates anagrams
"""

def lex_sort(word):
    """
    lexiografically sorts a word's characters
    """

    word_list = list(word)
    for i in range(len(word_list)):
        for j in range(len(word_list)):
            if word_list[i] < word_list[j]:
                tmp = word_list[i]
                word_list[i] = word_list[j]
                word_list[j] = tmp

    return "".join(word_list)
    

def validate(word, anagram):
    """
    checks if word is an anagram of another
    """
    if word == anagram:
        return False

    if lex_sort(word) == lex_sort(anagram):
        return True

    return False


def find_anagrams(word, candidates):
    """
    finds anagrams
    """
    solutions = []

    for candidate in candidates:
        if validate(word.lower(), candidate.lower()):
            solutions.append(candidate)
    
    return solutions
