# 13/06/2021
# Write a function called polysum that takes 2 arguments,
# n and s. This function should sum the area and square of
# the perimeter of the regular polygon. The function returns
# the sum, rounded to 4 decimal places.

from math import tan, pi

def polysum(n, s):
    '''
    :param n: integer
    :param s: integer or float
    :return: float, round 4 decimals
    '''
    area = (0.25 * n * s**2)/tan(pi/n)
    print(area)
    perimeter = n * s
    print(perimeter)
    return round((area + perimeter ** 2), 4)





