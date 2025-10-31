def count_factor_power(n, factor):
    power = 0
    while n % factor == 0:
        power = power + 1
        n = n // factor
    return power