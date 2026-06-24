def __is_triangle(sides):
    a, b, c = sides
    if (a + b < c) or (b + c < a) or (a + c < b):
        return False
    else:
        return True

def equilateral(sides):
    return True if (sides[0] == sides[1] == sides[2]) and sides[0] != 0 else False 


def isosceles(sides):
    if not __is_triangle(sides):
        return False
    is_isosceles = False
    if equilateral(sides):
        return True
    a, b, c = sides

    if (a == b) and c != a:
        return True
    elif (b == c) and b != a:
        return True
    elif (a == c) and b != a:
        return True
    else:
        return False

def scalene(sides):
    if not __is_triangle(sides):
        return False
    a, b, c = sides
    if not equilateral(sides) and not isosceles(sides):
        return True
    else:
        return False
