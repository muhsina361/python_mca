area_square = lambda side: side * side
area_rectangle = lambda length, width: length * width
area_triangle = lambda base, height: 0.5 * base * height

side = 4
length = 5
width = 6
base = 8
height = 10

print("Area of square:", area_square(side))
print("Area of rectangle:", area_rectangle(length, width))
print("Area of triangle:", area_triangle(base, height))
