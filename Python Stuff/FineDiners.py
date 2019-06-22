#Fine Diners
#Shehu Muhammad
#February 12, 2018

mealOne = float(input("What is the price of the first meal? "))
mealTwo = float(input("What is the price of the second meal? "))

tip = (mealOne + mealTwo) * 0.15

if(mealOne > 25 and mealTwo > 25):
    cost = mealOne + mealTwo + tip - 25
    print("The final bill is ", cost)

elif(mealOne > 25 and mealTwo < 25):
    cost = mealOne + tip
    print("The final bill is ", cost)

elif(mealOne < 25 and mealTwo > 25):
    cost = mealTwo + tip
    print("The final bill is ", cost)

elif(mealOne < 25 and mealTwo < 25 ):
        if(mealOne < mealTwo): 
            cost = mealTwo + tip
            print("The final bill is ",cost)
        else:
            cost = mealOne + tip
            print("The final bill is ",cost)


#Edward Freeman

#donald = float(input("Donald's Meal? "))
#melania = float(input("Melania's Meal? "))

#tip = .15 * (donald + melania)
#if(melania < donald):
    #cheap = melania
    #expensive = donald
#else:
    #cheap = donald
    #expensive = melania
#if(cheap < 25):
    #finalcost = expensive + tip
#else:
    #finalcost = expensive + cheap - 25 + tip
#print("The final cost is $",finalcost)
