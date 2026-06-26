def distance(strand_a, strand_b):

    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")

    i = 0
    distance = 0
    while i < len(strand_a):
        if strand_a[i] != strand_b[i]:
            distance += 1
        i += 1

    return distance
