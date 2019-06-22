# Shehu Muhammad
# Seuss Program
# February 27, 2018

number = int(input("Input a number between 1 and 45: "))

if(number >= 1 and number <=29):
    number = number + 2
    print("The date is March ",number,".", sep="")
    print("March", number)
elif(number > 29 and number <= 45):
    number = number - 29
    print("The date is April ",number,".", sep="") #space needed
    print("April", number) #no space needed
else:
    print("The date is out of the range of the program.")
    
