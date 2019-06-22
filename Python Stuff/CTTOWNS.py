# Population decliner problem
# Shehu Muhammad
# April 11, 2018

rfile=open("Connecticut.txt", "r")
wfile=open("DECLINERS.txt", "w")

for line in rfile:
    fields=line.split(",")
    town=(fields[0])
    pop1970=int(fields[1])
    pop1980=int(fields[2])
    pop1990=int(fields[3])
    pop2000=int(fields[4])

    if((pop1970 > pop1980) and (pop1970 > pop1990) and (pop1970 > pop2000)):
        if((pop1980 > pop1990) and (pop1980 > pop2000)):
            if(pop1990 > pop2000):
                print(town)
                wfile.write(town)
                wfile.write("\n")
    
rfile.close()
wfile.close()
print("That's all folks.")
    
