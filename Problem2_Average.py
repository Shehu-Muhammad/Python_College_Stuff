# Shehu Muhammad
# Problem 2 -Determine the average of three numbers and print back that and middle number
# May 7, 2018

num1 = float(input("What is the first number? "))
num2 = float(input("What is the second number? "))
num3 = float(input("What is the third number? "))

avg = (num1 + num2 + num3)/3

mid = int(num1)

if(mid == num2 and mid == num3):
    print("The middle number is ", mid,".",sep="")
elif(mid == num2 and (mid < num3 or mid > num3)):
    print("The middle number is ", mid,".",sep="")
elif((mid < num2 or mid > num2) and mid == num3):
    print("The middle number is ", mid,".",sep="")
elif(mid > num2 and mid > num3):
    if(num2 > num3):
        mid = int(num2)
        print("The middle number is ", mid,".",sep="")
    else:
        mid = int(num3)
        print("The middle number is ", mid,".",sep="")
elif(mid < num2 and mid < num3):
    if(num2 < num3):
        mid = int(num2)
        print("The middle number is ", mid,".",sep="")
    else:
        mid = int(num3)
        print("The middle number is ", mid,".",sep="")
elif((mid < num2 and mid > num3) or (mid > num2 and mid < num3)):
    print("The middle number is ", mid,".",sep="")
print("The average is ", round(avg,3),".",sep="")

