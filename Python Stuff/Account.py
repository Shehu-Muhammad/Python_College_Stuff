# Account Program
# Shehu Muhammad
# February 14, 2018

grade1 = int(input("What was the first grade? "))
grade2 = int(input("What was the second grade? "))
grade3 = int(input("What was the third grade? "))
grade4 = int(input("What was the fourth grade? "))

if(grade2 <= 50):
    print("You failed Part 1.")
    print("You failed Part 2.")
    print("You failed Part 3.")
    print("You failed Part 4.")
elif(grade1 >=75 and (grade2 <75 and grade3 <75 and grade4 <75)):
    print("You failed Part 1.")
    print("You failed Part 2.")
    print("You failed Part 3.")
    print("You failed Part 4.")       
elif(grade2 >=75 and (grade1 <75 and grade3 <75 and grade4 <75)):
    print("You failed Part 1.")
    print("You failed Part 2.")
    print("You failed Part 3.")
    print("You failed Part 4.")   
elif(grade3 >=75 and (grade1 <75 and grade2 <75 and grade4 <75)):
    print("You failed Part 1.")
    print("You failed Part 2.")
    print("You failed Part 3.")
    print("You failed Part 4.")  
elif(grade4 >=75 and (grade1 <75 and grade2 <75 and grade3 <75)):
    print("You failed Part 1.")
    print("You failed Part 2.")
    print("You failed Part 3.")
    print("You failed Part 4.")
elif(grade1 >= 75 and grade2 >= 75 and grade3 >=75 and grade4 <75):
    print("You passed Part 1.")
    print("You passed Part 2.")
    print("You passed Part 3.")
    print("You failed Part 4.")
elif(grade1 >= 75 and grade2 >= 75 and grade3 <75 and grade4 >=75):
    print("You passed Part 1.")
    print("You passed Part 2.")
    print("You failed Part 3.")
    print("You passed Part 4.")
elif(grade1 >= 75 and grade2 < 75 and grade3 >=75 and grade4 >=75):
    print("You passed Part 1.")
    print("You failed Part 2.")
    print("You passed Part 3.")
    print("You passed Part 4.")
elif(grade1 < 75 and grade2 >= 75 and grade3 >=75 and grade4 >=75):
    print("You failed Part 1.")
    print("You passed Part 2.")
    print("You passed Part 3.")
    print("You passed Part 4.")
elif(grade1 >= 75 and grade2 >= 75 and grade3 >=75 and grade4 >=75):
    print("You passed Part 1.")
    print("You passed Part 2.")
    print("You passed Part 3.")
    print("You passed Part 4.")
