import math

def Circle(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference                  # yha pr execution rukjayega
    print('hi')

a, c = Circle(2) 

print("Area of circle: ", a, "\nCircumference of circle: ", c)

# {:.2f} -> for 2 point precision
# {:f}   -> for 4 point precision
