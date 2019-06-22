# Poker Player Count
# Shehu Muhammad
# March 26, 2018

rfile=open("TextFiles/PokerChips.txt","r")
wfile=open("TextFiles/PokerPlayers.txt","w")

nameTotal=0
for line in rfile:
    fields=line.split(",")
    name=(fields[0])
    
    if(name is not None):
        nameTotal+=1
total= nameTotal
total=str(total)
wfile.write("The total number of poker player is: ")
wfile.write(total)
wfile.write(".")
print(nameTotal)
    
    
rfile.close()
wfile.close()
print("That's all folks.")
        
