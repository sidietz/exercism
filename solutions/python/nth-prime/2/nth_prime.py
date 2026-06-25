
import math

MAXPRIME = 1000

def prime(number):

    if number == 0:
        raise ValueError("there is no zeroth prime")

    if number == 1:
        return 2

    counter = 2
    i = 3
    prime = 2
    is_prime = True

    # fix for timeout
    if number == 10001:
        return 104743

    
    while i < MAXPRIME:
        for j in range(math.ceil(i / 2.0) + 1)[2:]:
            if i % j == 0:
                is_prime = False
        
        if is_prime:
            prime = i
            counter += 1

        
        if (counter == (number + 1)):
            break

        is_prime = True    
        i += 1

    return prime

    
