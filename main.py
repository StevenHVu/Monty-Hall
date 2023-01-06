# Python program to simulate the Monty Hall Problem - a better explanation can be found here: https://www.youtube.com/watch?v=4Lb-6rxZxx

# Importing random module for random number generation
import random

# Initialize a list named "doors" with three elements, each having a goat
doors = ['goat', 'goat', 'goat']

# Using ANSI excape codes to make it easier to see + change text color
print('\033[1;212m')

# Randomly change one of the doors into having the car and print out the doors
carIndex = random.randrange(0, 3)
print('The car is hidden behind door number', carIndex + 1)

doors[carIndex] = 'car'
print('The hidden items behind the doors are:', doors)

# Following the assumption: The host must always open a door that was not picked by the contestant
if (carIndex == 1):
    montyChoice = 2
else:
    montyChoice = 1

# Following the assumption: The host must always open a door to reveal a goat and never the car.
print('Monty opens door number', montyChoice + 1, 'which had a', doors[montyChoice])

# Following the assumption: The host must always offer the chance to switch between the originally chosen door and the remaining closed door.
print('Would you like to swap between your chosen door with the remaining closed door?')
print('Enter 1 to change choice to door number', carIndex + 1,'\nEnter 2 to keep original choice\n')
userChoice = input()

# Decide the prize for the user
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