#dice rolling program with GUI

print("Starting Program")

import random as r

#definitions
def cont():
        answer = raw_input("Do you want to roll again? (y/n):")
        answer = answer.lower()
        if answer == "y" or answer == "yes":
            return True
        else:
            return False


while True:
    numDice = raw_input("How many dice do you want to roll?:")

    dice = {}

    for count in range(1, int(numDice)+1):
        diceSides = raw_input("How many sides does dice number {} have?\n".format(count))
        dice[count] = int(diceSides)

    rolls = []

    for count in dice:
        print("Dice number {} has {} sides. Rolling now.".format(count, dice[count]))
        roll = r.randrange(1, dice[count])
        print("{}\n".format(roll))
        rolls += str(roll)

    total = 0

    for roll in rolls:
        total += int(roll)

    print("The total is {}!".format(total))
    con = cont()
    if con == False:
        raw_input("Program Ended! Hit Enter to Close Window")
        break
    else:
        continue
        

