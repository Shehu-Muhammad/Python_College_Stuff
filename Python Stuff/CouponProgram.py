# Triple Coupons Program
# Shehu Muhammad
# February 14, 2018

itemCost = float(input("How much will the item cost? "))
faceValue = float(input("How much is the face value of the coupon? "))

if(faceValue >= 1):
    finalCost = itemCost - faceValue
else:
    finalCost = itemCost - (3*faceValue)
if(finalCost < 0):
    finalCost = 0
print("The final cost of the item is ", format(finalCost,'.2f'), ".", sep="")

