def find_next_prime_factor(n, start):
    if start < 2:
        start = 2
    i = start
    while i <= n:
        if n % i == 0: 
            z = 2
            for z in range(2, i):
                if i % z == 0:
                    break  
                z = z + 1
            if z * z > i:  
                return i
        i = i + 1
    return n

