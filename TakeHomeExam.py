# Shehu Muhammad
# Take Home Exam 
# April 8, 2018

hour1 = int(input("What hour did the tournament begin? "))
minute1 = int(input("What minute did the tournament begin? "))
hour2 = int(input("What hour did the tournament end? "))
minute2 = int(input("What minute did the tournament end? "))

flag = 0

if((hour1 < 0 or hour1 > 23) or (hour2 < 0 or hour2 > 23) or (minute1 <0 or minute1 > 59) or (minute2 < 0 or minute2 > 59)):
    flag = 1
    if(flag):
        if(hour1 < 0 or hour1 > 23):
            print("Hour 1 must be between 0 and 23.")
        if(minute1 < 0 or minute1 > 59):
            print("Minute 1 must be between 0 and 59.")
        if(hour2 < 0 or hour2 > 23):
            print("Hour 2 must be between 0 and 23.")
        if(minute2 < 0 or minute2 > 59):
            print("Minute 2 must be between 0 and 59.")

elif((hour1 > hour2) or (hour1 == hour2 and minute1 > minute2)):
    print("The tournament cannot end before it begins.")
	
else:
    if(minute1 > minute2):
        hour2 = hour2 - 1
        minute2 = minute2 + 60
        hours = hour2 - hour1
        minutes = minute2 - minute1
    else:
        hours = hour2 - hour1
        minutes = minute2 - minute1
    print("The tournament lasted ",hours," hours and ", minutes," minutes.")
