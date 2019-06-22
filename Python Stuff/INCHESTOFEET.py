#INCHESTOFEET Program
#Shehu Muhammad
#January 31, 2018

feet = float(input("How many feet? "))
inches = float(input("How many inches? "))

convertFeet = feet*12
totalInches = convertFeet + inches

print("The total number of inches is ", totalInches, ".", sep="")

#Checks if the total inches is even or odd

if(totalInches%2==0):
    print("The number of total inches is ", totalInches, " even.")
else:
    print("The number of total inches is ", totalInches, " odd.")
    



                     
