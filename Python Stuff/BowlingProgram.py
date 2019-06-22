# Bowling Perfect Program
# Shehu Muhammad
# March 28, 2018

rfile=open("TextFiles/BOWLING.txt","r")
wfile=open("TextFiles/TWO300S.txt","w")

for line in rfile:
    fields=line.split(",")
    name=(fields[0])
    score1=int(fields[1])
    score2=int(fields[2])
    score3=int(fields[3])
        
    if(score1 == 300 and score2 == 300 and score3 != 300):
        print(name)
        wfile.write(name)
        wfile.write("\n")
    elif(score1 == 300 and score3 == 300 and score2 != 300):
        print(name)
        wfile.write(name)
        wfile.write("\n")   
    elif(score2 == 300 and score3 == 300 and score1 != 300):
        print(name)
        wfile.write(name)
        wfile.write("\n")
            
rfile.close()
wfile.close()
print("That's all folks.")
