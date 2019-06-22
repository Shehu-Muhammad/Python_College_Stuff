# Shehu Muhammad
# Jelly Bean Program
# February 28, 2018

lbs = float(input("How many pounds are your jelly beans? "))

if(1 <= lbs <= 6):
    cost = lbs * 4
elif(7 <= lbs <= 12):
    cost = lbs * 3
elif(13 <= lbs <= 20):
    cost = lbs * 2
elif(lbs >= 21):
    cost = lbs * 1.5
elif(lbs < 0):
    print("Call a cop.")
else:
    print("Get more jelly beans.")
print("It costs $",format(cost,'.2f'),".", sep="")

