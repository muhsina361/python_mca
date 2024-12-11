from Math_operations.basic import arithamatic
from Math_operations.geometry import area
 #basic operations
print("arithematic operations:")
print("5+3=",arithamatic.add(5,3))
print("10-7=",arithamatic.subtract(10,7))
print("5*3=",arithamatic.multiply(5,3))
print("8/2=",arithamatic.divide(8,2))
print("8/0=",arithamatic.divide(8,0))

#area calculations

print("\naraea calculations:")
print("rectangle(length=5,width=3):",area.rectangle_area(5,3))
print("circle(radius=7):",area.circle_area(7))
print("triangle(base4,height=5):",area.triangle_area(4,5))
