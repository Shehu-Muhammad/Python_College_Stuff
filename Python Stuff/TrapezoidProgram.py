#Trapezoid Program
# Finds the area of a trapezoid
# Shehu Muhammad

upperbase = float(input("What is the upper base? "))
lowerbase = float(input("What is the lower base? "))

height = float(input("What is the height? "))

area = ((upperbase + lowerbase) * height)/2

#print("You told me the upper base was ", upperbase)
#print("the lower base was ", lowerbase)
#print("and the height was ", height)

print("You told me the upper base was ", upperbase, ", the lower base was ", lowerbase, ", and the height was ", height)

print("Therefore the area of the trapezoid is ", area)
print("Therefore the area of the trapezoid is ", round(area,2))
