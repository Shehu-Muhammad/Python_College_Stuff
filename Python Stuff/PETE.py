#PETE Program
#Shehu Muhammad
#February 12, 2018

Grade1 = float(input("What is grade 1? "))
Grade2 = float(input("What is grade 2? "))
Grade3 = float(input("What is grade 3? "))

if(Grade1 > Grade2 and Grade1 > Grade2):
    FinalGrade = (Grade2 + Grade3)/2
elif(Grade2 > Grade1 and Grade2 > Grade3):
    FinalGrade = (Grade1 + Grade3)/2
elif(Grade3 > Grade1 and Grade3 > Grade2):
    FinalGrade = (Grade1 + Grade2)/2
print("The final grade is: ",FinalGrade)


