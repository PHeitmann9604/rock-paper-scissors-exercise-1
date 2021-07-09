
import random

print("Rock, Paper, Scissors, Shoot!")

# ask for a user input
# source *put google doc here*
#x = input('______')

x = input("Please choose one of 'rock', 'paper', 'scissors': ")
print(x)

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
print(random.choice(valid_options))

c = random.choice(valid_options)
print("Computer Chose: ", c)




#Determine the winner