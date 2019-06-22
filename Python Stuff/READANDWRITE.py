#Read from a file
#Shehu Muhammad
#February 3, 2018

data = open('C:\\Users\\Shehu\\Documents\\DewDropTextFile.csv', 'r')

with open('C:\\Users\\Shehu\\Documents\\DewDropTextFile.csv', 'r') as data:
    reader = data.read()
    print(reader)
    
data.closed
True

