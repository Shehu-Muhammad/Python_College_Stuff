# Shehu Muhammad
# Basketball Program
# February 27, 2018

feet = int(input("Enter the feet for the height: "))
inches = int(input("Enter the inches for the height: "))

while(inches >= 12):
    inches = inches - 12
    feet = feet + 1
if(feet <= 0 and inches <= 0):
    print("Your height is a lie. You cannot play in the league.")
elif((feet > 6 or (feet >= 6 and inches > 4))):
    print("You cannot play in the league.")
else:
    print("You can play in the league.")
print("You are ", feet," feet and ",inches, " inches.")

# Basketball
# Edward Freeman
#feet=int(input("How many feet? "))
#inches= int(input("How many inches"))
#totalinches=12*feet + inches
#if (totalinches<=76):
    #print("You can play in the league")
#else:
    #print("You cannot play in the league")
