# Guess my number
# Shehu Muhammad

import random
import math
random.seed()

randomNumber = math.floor(random.random() * 100) + 1 # generates a random number between 1 and 100
guess = 0                                            # initializes guess to zero
count = 0                                            # initializes count to 0

while (randomNumber != guess):                       # loops until guess is equal to random number
    count = count+1                                  # increments count by 1 when guess is wrong 
    guess = int(input("Guess my number: "))          # askes user for a guess
    
    if (guess < randomNumber):                       # checks if guess is lower than random number 
        print("Higher!")                             # prompts user for a higher guess
        
    elif(guess > randomNumber):                      # checks if guess is higher than random number 
        print("Lower!")                              # prompts user for a lower guess
        
print("Correct! " + str(count) + " tries.")          # Prints "Correct" and number of tries counted until the user guessed the random number
              
