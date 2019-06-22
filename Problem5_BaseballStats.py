# Shehu Muhammad
# Problem 5 -Baseball (name, doubles, triples, home runs)
# May 7, 2018

rfile=open("BASEBALLFINAL.txt","r")
wfile=open("MANYHITS.txt","w")

for line in rfile:
    fields=line.split(",")
    name=(fields[0])
    doubles=int(fields[1])
    triples=int(fields[2])
    homeRuns=int(fields[3])

    if((doubles + triples + homeRuns) > 78):
        print(name)
        wfile.write(name)
        wfile.write("\n")
rfile.close()
wfile.close()
    
