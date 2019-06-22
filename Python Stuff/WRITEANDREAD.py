#Writing to a file
#Shehu Muhammad
#February 5, 2018

data = open('C:\\Users\\Shehu\\Documents\\DewDropTextFile.csv', 'w')

with open('C:\\Users\\Shehu\\Documents\\DewDropTextFile.csv', 'w') as data:
    writer = data.write()
    print("Hello World from written file.")

data.closed
True
    
