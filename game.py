
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

#if invalid rerun the user input

    x = input("Please choose one of 'rock', 'paper', 'scissors': ")

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

#If a tie rerun the game

#source for while stmt: https://docs.python.org/3/reference/compound_stmts.html#while

while (x == c):
    print ("TIE! Please try again")
    x = input("Please choose one of 'rock', 'paper', 'scissors': ")

    if (x == "rock") or (x == "paper") or (x == "scissors"):
        print ("VALID")
    else:
        print("OOPS INVALID, Please try again")
        x = input("Please choose one of 'rock', 'paper', 'scissors': ")

    print ("User Chose: ", x)

    c = random.choice(valid_options)

    print("Computer Chose: ", c) 

if ((x == 'rock') and (c == 'scissors')) or ((x == 'scissors') and (c == 'paper')) or ((x == 'paper') and (c == 'rock')):
    print ("USER WINS! Congratulations!")
else:
    print ("Computer Wins =( Please try again")

    