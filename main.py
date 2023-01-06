# Python program to simulate the Monty Hall Problem - a better explanation can be found here: https://www.youtube.com/watch?v=4Lb-6rxZxx

# Importing random module for random number generation
import random

# Initialize the doors with default goat
doors = ['goat', 'goat', 'goat']

# Making it easier to see + changing text color
print('\033[1;212m')

# Randomly change one of the doors into having the car and print out the doors
carIndex = random.randrange(0, 3)
print('The car is hidden behind door number', carIndex + 1)

doors[carIndex] = 'car'
print('The hidden items behind the doors are:', doors)

# Monty Hall
if (carIndex == 1):
    montyChoice = 2
else:
    montyChoice = 1

print('Monty opens door number', montyChoice + 1, 'which had a', doors[montyChoice])

# Ask the user if they want to swap choices
print('Would you like to swap between your chosen door with the remaining closed door?')
userChoice = input('Enter 1 for Yes, 2 for No\n')

# Decide the prize
if (userChoice == '1'):
    if (carIndex == 0):
        print('You won a goat!')
    else:
        print('You won the car!')
elif (userChoice == '2'):
    if (carIndex != 0):
        print('You won a goat!')
    else:
        print('You won the car!')
   
# Resetting font color     
print('\033[1;0m')