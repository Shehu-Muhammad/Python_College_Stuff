# Over 1170 at the diner
# Edward Freeman
ffile=open("TextFiles/thediner.txt","r")            # open the file thediner.txt to read and refer to it as ffile
ffile2=open("TextFiles/over1170.txt","w")           # open a new file called over 1170.txt for writing purposes.
                                                    # and refer to this file as ffile2.
for line in ffile:                                  # for every line in the file (until the end), do the indented lines.
    fields=line.split(",")                          # start a new field every time you reach a comma.
    ddate=(fields[0])                               # ddate is the first field in the record (fields[0]), a text field
    breakfasts=int(fields[1])                       # breakfasts is the second field in the record and is an integer
    lunches=int(fields[2])                          # lunches is the third field in the record and is an integer
    if(5*breakfasts+7*lunches>1170):                # Standard if statement. If receipts are more than 1170
        print(ddate)                                # print the date in Python
        ffile2.write(ddate)                         # Write the date to ffile2, over1170.txt.
        ffile2.write("\n")                          # Start a new line in ffile2, over1170.txt
ffile.close()                                       # Close the data file
ffile2.close()                                      # Close the file with the results.
print("That's all folks.")                          # Means nobody met the criteria or a mistake was made
