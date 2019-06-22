#Welding Program
#Shehu Muhammad
#February 12, 2018

pipe1Feet = int(input("How long is the first pipe in feet? "))
pipe1Inches = int(input("How long is the first pipe in inches? "))

pipe2Feet = int(input("How long is the second pipe in feet? "))
pipe2Inches = int(input("How long is the second pipe in inches? "))

totalInches = pipe1Inches + pipe2Inches

if(totalInches >= 12):
    totalInchesToFeet = totalInches//12
    inches = totalInches%12
    totalFeet = pipe1Feet + pipe2Feet + totalInchesToFeet
    print("The total number of feet is ",totalFeet, ", and the total number of inches is ",inches)
else:
    totalFeet = pipe1Feet + pipe2Feet
    print("The total number of feet is ",totalFeet, ", and the total number of inches is ",totalInches)

# Willie the Welder
# Edward Freeman
# feet1 = int(input("First Feet - How Many"))
# inches1 = int(input("First Inches - How Many"))
# feet2 = int(input("Second Feet - How Many"))
# inches2 = int(input("Second Inches - How Many"))
# totalfeet= feet1 + feet2
# totalinches = inches1+inches2
# if (totalinches > 11):
     # totalfeet = totalfeet +1
     # totalinches = totalinches-12
# print(totalfeet, "feet")
# print(totalinches, " inches")
