# The movies
# Edward Freeman
age=int(input("How old are you? "))
if (1 <= age <=11):
     print("$4.00")
elif (12 <= age <= 62):
     print("$12.00")
elif (63 <= age <= 89):
     print("$6.00")
elif (age >=90):
     print("$2.00")
else:
     print("Hey stupid! You haven't been born yet")
