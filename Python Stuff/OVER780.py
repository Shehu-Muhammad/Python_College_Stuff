# Over 780 on SATs
# Shehu Muhammad
# March 24, 2018

rfile=open("TextFiles/Scores2.txt","r")
wfile=open("TextFiles/OVER780.txt","w")

for line in rfile:
    fields=line.split(",")
    name=(fields[0])
    part1 = int(fields[1])
    part2 = int(fields[2])
    part3 = int(fields[3])

    if((part1 + part2 + part3)/3 > 780):
        print(name)
        wfile.write(name)
        wfile.write("\n")
rfile.close()
wfile.close()
print("That's all folks.")
    
