"""
Implement a function named solve_quadratic which takes three arguments: a, b, and c, which are the coefficients of the quadratic equation. 
This function should return the solution written in readME file. You can assume that the quadratic equation will always have a solution.
"""

def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    root1 =( -b - discriminant**0.5) / 2*a
    root2 =( -b + discriminant**0.5) / 2*a
    return root1, root2

