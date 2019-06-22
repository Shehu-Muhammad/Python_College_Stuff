# Shehu Muhammad
# Problem 3 -Displays the sum of the even numbers from 2 to 126
# May 7, 2018

total = 0
for x in range(0,127,2):
    total = x + total
print("The sum of the even numbers from 2 to 126 is ", total,".",sep="")
