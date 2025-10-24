"""
Part a) Implement a function named distance, which takes four arguments: x1, y1, x2, and y2, representing the coordinates of two points (x1, y1) and (x2, y2). 
This function should return the Euclidean distance between these two points.

Part b) Implement a function named area_from_sides, which takes three arguments: a, b, and c, which are the lengths of the three sides. 
This function should return the area of the triangle.

Part c) Implement a function named area_from_vertices, which takes six arguments: x1, y1, x2, y2, x3, y3, representing the coordinates of three vertices (x1, y1), (x2, y2), and (x3, y3). 
This function should return the area of the triangle.
"""

def distance(x1, y1, x2, y2):
    return((x2 - x1)**2 + (y2 - y1)**2)** 0.5
def area_from_sides(a, b, c):
    s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5
def area_from_vertices(x1, y1, x2, y2, x3, y3):
    area = (x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2
    if area < 0:
        area= -area
    return round(area, 2)
#test

