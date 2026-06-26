"""
matches brackets
"""

CHARS = ['(', ')', '[', ']', '{', '}']

def validate(condensed):
    """
    validates a condensed list using a stack approach
    """

    stack = []

    for e in condensed:
        if not stack:
            if e in CHARS[::2]:
                pass
            else:
                return False
        if e in CHARS[::2]:
            stack.append(e)
        elif e in CHARS[1::2]:
            if e == ')':
                if stack[len(stack) - 1] == '(':
                    stack.pop()
                else:
                    return False
            if e == ']':
                if stack[len(stack) - 1] == '[':
                    stack.pop()
                else:
                    return False
            if e == '}':
                if stack[len(stack) - 1] == '{':
                    stack.pop()
                else:
                    return False

    return True
    

def is_paired(input_string):
    """
    checks if brackets, braces and parantheses are paired
    """

    bracket_depth = 0
    braces_depth = 0
    parentheses_depth = 0

    condensed = []

    for e in input_string:
        if e not in CHARS:
            pass
        else:
            condensed.append(e)
            if e == '(':
                parentheses_depth += 1
            elif e == ')':
                parentheses_depth -= 1
            elif e == '[':
                bracket_depth += 1
            elif e == ']':
                bracket_depth -= 1
            elif e == '{':
                braces_depth += 1
            elif e == '}':
                braces_depth -= 1
            else:
                pass

    if braces_depth != 0:
        return False
    if bracket_depth != 0:
        return False
    if parentheses_depth != 0:
        return False

    return validate(condensed)
    
                