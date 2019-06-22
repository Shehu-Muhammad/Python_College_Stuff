#Shehu Muhammad
#Take Home Exam
#April 4, 2018

hour1 = int(input("What hour did the tournament begin? "))
minute1 = int(input("What minute did the tournament begin? "))
hour2 = int(input("What hour did the tournament end? "))
minute2 = int(input("What minute did the tournament end? "))

if((hour1 < 0 or hour1 > 23) and (hour2 < 0 or hour2 > 23) and (minute1 < 0 or minute1 > 59) and (minute2 < 0 or minute2 > 59)):
	print("Hour 1 must be between 0 and 23.\nMinute 1 must be between 0 and 59.\nHour 2 must be between 0 and 23.\nMinute 2 must be between 0 and 59.")
	
elif((hour1 > 0 or hour1 < 23) and (hour2 < 0 or hour2 > 23) and (minute1 < 0 or minute1 > 59) and (minute2 < 0 or minute2 > 59)):
	print("Hour 2 must be between 0 and 23.\nMinute 1 must be between 0 and 59.\nMinute 2 must be between 0 and 59.")
	
elif((hour1 > 0 or hour1 < 23) and (hour2 < 0 or hour2 > 23) and (minute1 > 0 or minute1 < 59) and (minute2 < 0 or minute2 > 59)):
	print("Hour 2 must be between 0 and 23.\nMinute 2 must be between 0 and 59.")

elif((hour1 > 0 or hour1 < 23) and (hour2 < 0 or hour2 > 23) and (minute1 < 0 or minute1 > 59) and (minute2 > 0 or minute2 < 59)):
	print("Hour 2 must be between 0 and 23.\nMinute 1 must be between 0 and 59.")

elif((hour1 > 0 or hour1 < 23) and (hour2 < 0 or hour2 > 23) and (minute1 > 0 or minute1 < 59) and (minute2 > 0 or minute2 < 59)):
	print("Hour 2 must be between 0 and 23.")
	
elif((hour1 < 0 or hour1 > 23) and (hour2 > 0 or hour2 < 23) and (minute1 < 0 or minute1 > 59) and (minute2 < 0 or minute2 > 59)):
	print("Hour 1 must be between 0 and 23.\nMinute 1 must be between 0 and 59.\nMinute 2 must be between 0 and 59.")
	
elif((hour1 < 0 or hour1 > 23) and (hour2 > 0 or hour2 < 23) and (minute1 > 0 or minute1 < 59) and (minute2 < 0 or minute2 > 59)):
	print("Hour 1 must be between 0 and 23.\nMinute 2 must be between 0 and 59.")
	
elif((hour1 < 0 or hour1 > 23) and (hour2 > 0 or hour2 < 23) and (minute1 < 0 or minute1 > 59) and (minute2 > 0 or minute2 < 59)):
	print("Hour 1 must be between 0 and 23.\nMinute 1 must be between 0 and 59.")
	
elif((hour1 < 0 or hour1 > 23) and (hour2 > 0 or hour2 < 23) and (minute1 > 0 or minute1 < 59) and (minute2 > 0 or minute2 < 59)):
	print("Hour 1 must be between 0 and 23")

elif((hour1 < 0 or hour1 > 23) and (hour2 < 0 or hour2 > 23) and (minute1 > 0 or minute1 < 59) and (minute2 < 0 or minute2 > 59)):
	print("Hour 1 must be between 0 and 23.\nHour 2 must be between 0 and 23.\nMinute 2 must be between 0 and 59.")
	
elif((hour1 < 0 or hour1 > 23) and (hour2 < 0 or hour2 > 23) and (minute1 < 0 or minute1 > 59) and (minute2 > 0 or minute2 < 59)):
	print("Hour 1 must be between 0 and 23.\nMinute 1 must be between 0 and 59.\nHour 2 must be between 0 and 23.")
	
elif((hour1 < 0 or hour1 > 23) and (hour2 < 0 or hour2 > 23) and (minute1 > 0 or minute1 < 59) and (minute2 > 0 or minute2 < 59)):
	print("Hour 1 must be between 0 and 23.\nHour 2 must be between 0 and 23.")
	
elif((hour1 > 0 or hour1 < 23) and (hour2 > 0 or hour2 < 23) and (minute1 < 0 or minute1 > 59) and (minute2 < 0 or minute2 > 59)):
	print("Minute 1 must be between 0 and 59.\nMinute 2 must be between 0 and 59.")
	
elif((hour1 > 0 or hour1 < 23) and (hour2 > 0 or hour2 < 23) and (minute1 > 0 or minute1 < 59) and (minute2 < 0 or minute2 > 59)):
	print("Minute 2 must be between 0 and 59")
	
elif((hour1 > 0 or hour1 < 23) and (hour2 > 0 or hour2 < 23) and (minute1 < 0 or minute1 > 59) and (minute2 > 0 or minute2 < 59)):
	print("Minute 1 must be between 0 and 59")
	
elif(hour1 > hour2 or (hour1 == hour2 and minute2 < minute1)):
	print("The tournament cannot end before it begins.")
        
elif((hour1 > 0 or hour1 < 23) and (hour2 > 0 or hour2 < 23) and (minute1 > 0 or minute1 < 59) and (minute2 > 0 or minute2 < 59)):
	if(minute1 > minute2):
		hour2 = hour2 - 1
		minute2 = minute2 + 60
		hours = hour2 - hour1
		minutes = minute2 - minute1
	elif((minute1 == minute2) or (minute1 < minute2)):
		hours = hour2 - hour1
		minutes = minute2 - minute1
	print("The tournament lasted ",hours," hours and ", minutes," minutes.")



	


	

