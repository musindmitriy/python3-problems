
import math


def square(a):

    p = 4 * a
    s = a ** 2
    diag = a * math.sqrt(2)  # можно diag = math.hypot(a, a)

    return p, s, diag
