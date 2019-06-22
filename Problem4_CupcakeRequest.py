# Shehu Muhammad
# Problem 4 -Requests the number of cupcakes ordered and displays the total cost
# May 7, 2018

orders = int(input("What are the total number of cupcake orders? "))
cost = 0
small = 0.75
large = 0.70
if(orders <= 99 and orders>=1):
    cost = cost + (orders*small)
elif(orders >= 100):
    cost = cost + (orders*large)
else:
    print("No cupcakes were ordered.")
print("The total cost for the cupcakes ordered is $",format(cost,'.2f'),".",sep="")


