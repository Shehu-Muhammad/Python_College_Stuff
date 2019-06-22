# Shehu Muhammad
# RADIOFLYER Program
# February 26, 2018

singles = int(input("How many singles do you have? "))
fives = int(input("How many fives do you have? "))
tens = int(input("How many tens do you have? "))

fives = fives * 5
tens = tens * 10

cost = singles + fives + tens

goal = 95

final = goal - cost

if(final <= 0):
    print("You have enough money to buy the wagon.")
else:
    print("You have $",cost,". You need $",final,".", sep="")


