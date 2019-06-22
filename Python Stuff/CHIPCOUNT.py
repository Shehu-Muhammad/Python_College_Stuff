# Chip Count Program
# Shehu Muhammad
# March 26, 2018

rfile=open("TextFiles/Pokerchips.txt","r")
wfile=open("TextFiles/OVER1200.txt","w")

for line in rfile:
    fields=line.split(",")
    name=(fields[0])
    dollarChips= int(fields[1])
    fiveDChips= int(fields[2])
    tenDChips=int(fields[3])
    twentyFiveDChips=int(fields[4])
    hundredDChips=int(fields[5])
    
    fiveDChips= fiveDChips * 5
    tenDChips = tenDChips * 10
    twentyFiveDChips = twentyFiveDChips * 25
    hundredDChips = hundredDChips * 100
    
    if((dollarChips+fiveDChips+tenDChips+twentyFiveDChips+hundredDChips)>=1200):
        print(name)
        wfile.write(name)
        wfile.write("\n")
rfile.close()
wfile.close()
print("That's all folks.")
    
