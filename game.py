
import random

print("Rock, Paper, Scissors, Shoot!")

# ask for a user input
# source: https://docs.python.org/3/library/functions.html
#x = input('______')

x = input("Please choose one of 'rock', 'paper', 'scissors': ")

# Validate a user input

if (x == "rock") or (x == "paper") or (x == "scissors"):
    print ("VALID")
else:
    print("OOPS INVALID, Please try again")
    exit()

print ("User Chose: ", x)

#Generate a computer choice
#source: https://stackoverflow.com/questions/306400/how-to-randomly-select-an-item-from-a-list
#source: https://docs.python.org/3/library/random.html

# import random
# 
# foo = ['a', 'b', 'c', 'd', 'e']
# print(random.choice(foo))

valid_options = ['rock', 'paper', 'scissors']
c = random.choice(valid_options)

print("Computer Chose: ", c)

#Determine the winner
if (x == c):
    print ("TIE")
    x = input("Please choose one of 'rock', 'paper', 'scissors': ")

    if (x == "rock") or (x == "paper") or (x == "scissors"):
        print ("VALID")
    else:
        print("OOPS INVALID, Please try again")
        exit()
    
    print ("User Chose: ", x)
    
    valid_options = ['rock', 'paper', 'scissors']
    c = random.choice(valid_options)
    
    print("Computer Chose: ", c) 

if (x == 'rock') and (c == 'scissors'):
    print ("USER WINS")
elif (x == 'scissors') and (c == 'paper'):
    print ("USER WINS")
elif(x == 'paper') and (c == 'rock'):
    print ("USER WINS")
else:
    print ("Computer Wins")

    
#source:https://stackoverflow.com/questions/39174178/restart-python-program-within-and-if-statement-not-complex


