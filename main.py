# Python program to simulate the Monty Hall Problem - a better explanation can be found here: https://www.youtube.com/watch?v=4Lb-6rxZxx

# Importing random module for random number generation
import random

# Global default values
monty = 'Monty'
car = 'a car'
goat = 'a goat'

def customSettings():
    # Using ANSI excape codes to make it easier to see + change text color
    print('\n\033[1;37mWould you like to change the default values? (name of the host and prize)')
    customInput = input('1) Default settings | 2) Change settings\n')
    if (customInput == '2'):
        global monty, car, goat
        monty = input('\nEnter the name of the host: ')
        car = input('\nEnter what you want as a prize: ')
        goat = input('\nEnter something you wish you don\'t really want: ')
    return

# This function calculates which door of the three to open after the user selects a door
# Monty should pick the door that does not contain the car + is not the door picked by the user
def determineMontyChoice(userChoice, carIndex):
    carDoor = carIndex + 1
    montyDoor = carDoor
    # If the user's original choice contains the car, we want Monty to pick any other door randomly
    if (userChoice == carDoor):
        while (montyDoor == carDoor):
            montyDoor = random.randrange(1,3)
    # Otherwise, of the two doors, we want Monty to pick the one containing a goat
    else:
        i = 1
        for i in range(1,4): # ex: range(3, 6) creates a sequence of numbers from 3 to 5
            if (i != carDoor and i != userChoice):
                montyDoor = i
    return montyDoor

# This function finds the door that is not picked by Monty AND by the user
def findRemainingDoor(montyChoice, userChoice):
    remainingDoor = 0
    i = 1
    for i in range (1,4):
        if (i != montyChoice and i != userChoice):
            remainingDoor = i
    return remainingDoor

# This function will output the contents behind the doors, assuming they are in debugging mode
def debugText(carIndex, doors, debugFlag):
    if (int(debugFlag) == 2):
        print('\033[1;34m')
        print('The hidden items behind the doors are:', doors)
        print(car, 'is hidden behind door number', carIndex + 1)
        print('\033[1;37m', end='')
    return

# This function
def chooseRun():
    print('\033[1;32mWhat kind of run would you like to do?')
    chooseInput = input('1) Standard run | 2) Experimental Run\n')
    
    # For fun function to change around the default host name and prizes
    customSettings()
    
    if (int(chooseInput) == 1):
        standardRun()
    elif (int(chooseInput) == 2):
        experimentalRun()
    return

def standardRun():    
    # Flag for debugging mode
    debugFlag = int(0)

    print('\nWould you like to work in debug mode? 1) Default mode | 2) Debugging mode')
    debugFlag = input()

    # Initialize a list named "doors" with three elements, each having a goat
    doors = [goat, goat, goat]

    # Randomly change one of the doors into having the car and print out the doors
    carIndex = random.randrange(0, 2)
    doors[carIndex] = car

    # Print out hidden info if debug flag is set to TRUE
    debugText(carIndex, doors, debugFlag)

    # Explaining the doors and their names
    unknownDoors = ['Door 1', 'Door 2', 'Door 3']
    print('\nThere are three doors but you don\'t know which door holds the prize.\n', unknownDoors)
    
    # Allow the user to choose what door to pick
    userChoice = input('\nWhat door would you like to choose?\n')

    # Following the assumption: The host must always open a door that was not picked by the contestant
    montyChoice = determineMontyChoice(int(userChoice), carIndex)

    # Following the assumption: The host must always open a door to reveal a goat and never the car.
    print('\n\033[1;33m' + monty,'opened Door', montyChoice, 'which was revealed to have', doors[montyChoice - 1] + '!\n')

    unknownDoors[montyChoice - 1] = doors[montyChoice - 1]
    print(unknownDoors)
    
    # Find the remaining door that has not been opened
    remainingDoor = findRemainingDoor(montyChoice, int(userChoice))

    # Following the assumption: The host must always offer the chance to switch between the originally chosen door and the remaining closed door.
    print('\033[1;37mWould you like to swap between your chosen door with the remaining closed door?')
    print('Enter 1 to keep Door', userChoice,'\nEnter 2 to switch to Door', remainingDoor)
    userInput = input()

    # Decide the prize for the user
    print('\033[1;33m')
    if (userInput == '2'):
        print(monty,'opens door', remainingDoor, 'and behind the door turns out to be ...\n')
        if (carIndex + 1 == int(userChoice)):
            print('\033[1;0m' + goat + '...')
        else:
            print('\033[1;35m' + car + '! :D')
    elif (userInput == '1'):
        print(monty, 'opens door', userChoice, 'and behind the door turns out to be ...\n')
        if (carIndex + 1 != int(userChoice)):
            print('\033[1;0m' + goat + '...')
        else:
            print('\033[1;35m' + car + '! :D')
    print('\033[1;37m')
    return

# This function prompts the user if they would like to do another run or quit the program
def loop(loopFlag):
    print('Would you like to go again?')
    loopInput = input('1) Go again | 2) Quit\n')
    if (int(loopInput) == 2):
        loopFlag = 0
    return loopInput

# 
def experimentalRun():
    
    return

# Main program that will be executed at the beginning
def main():
    loopFlag = 1
    while (int(loopFlag) == 1):
        # Give option select a kind of run to do 
        chooseRun()
        
        # Give option to loop
        loopFlag = loop(loopFlag)
        
        # Resetting font color     
        print('\033[1;0m')
    return
    
# Run program    
main()
        
    