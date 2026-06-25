def sum_of_multiples(limit, multiples):

    values = []
    for i in range(1, limit):
        for m in multiples:
            if m == 0:
                continue
            if (i % m) == 0:
                values.append(i)

    if not values:
        return 0

    value_set = set(values)

    result = 0
    for element in list(value_set):
        result += element
    
    return result
