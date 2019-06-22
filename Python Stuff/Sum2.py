# Sum 1/3 + 1/7 + 1/11 + 1/15....1/403
# Shehu Muhammad
# March 19, 2018

tally = 0
for x in range(3,404,4):
    tally = tally + (1/x)
print(round(tally,6))
