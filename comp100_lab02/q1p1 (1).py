def find_next_prime_factor(n, start):
    
    def prime_number(x):
        if x < 2:
            return False
        for i in range(2, int(x**0.5) + 1):
             if i % 2 == 0:
                return False
        return True 

    for i in range(start, n + 1):
        if n % i == 0 and prime_number(i):
            return i
        
        
        
        
            
            
        
        
    


    return n
print(find_next_prime_factor(84, 2))   # 2
print(find_next_prime_factor(84, 3))   # 3
print(find_next_prime_factor(91, 5))   # 7
print(find_next_prime_factor(97, 2))   # 97 (çünkü 97 asal)
print(find_next_prime_factor(120, 7))