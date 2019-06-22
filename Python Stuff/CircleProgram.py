# Circle Program
# Finds the area of a circle if we know the radius 
# Shehu Muhammad
import math 
radius = float(input("What is the radius of the circle? "))

#pi = 3.1416
pi = math.pi

area = pi * (radius**2)
#area = pi * (math.expm1(radius)

print("You told me the circle has a radius of ", radius)
print("The area of the circle is ", area)
print("The area of the circle is ", round(area,3))
