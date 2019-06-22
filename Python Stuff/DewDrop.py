#Dew Drop
#Shehu Muhammad
#February 2, 2018
                 
cost = float(input("What was the cost of the meal? "))
tip = cost * 0.182
finalCost = cost + tip

print("The tip is 18.2% of $", format(cost,'.2f'), " so it came out to $", format(tip,'.2f'), ".", sep="")
print("The final cost of the meal is ", format(finalCost,'.2f'), ".", sep="")

print("The tip is 18.2% of $",round(cost,2), " so it came out to $", format(tip,'.2f'), ".", sep="")
print("The final cost of the meal is ", round(finalCost,2), ".", sep="")
    
    
