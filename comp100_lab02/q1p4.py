from q1p1 import find_next_prime_factor
from q1p2 import count_factor_power
from q1p3 import format_factor
def format_prime_factors(n):
    factorization_string = ""
    start_factor = 2
    while start_factor <= n:
        factor = find_next_prime_factor(n, start_factor)
        power = count_factor_power(n, factor)
        if power > 0:
            if factorization_string != "":
                factorization_string = factorization_string + " * "
            factorization_string = factorization_string + format_factor(factor, power)
            temp = 1
            k = 0
            while k < power:
                temp = temp * factor
                k = k + 1
            n = n // temp
            start_factor = factor + 1
        else:
            start_factor = start_factor + 1
    return factorization_string
#prime factor finder