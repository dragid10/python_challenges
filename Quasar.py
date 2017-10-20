from random import randint
from time import sleep

class var:
    yourCash = 0
    houseCash = 0

def play(cash):
    var.yourCash = var.yourCash - cash
    var.houseCash = var.houseCash + cash
    startNum = randint(1,4)
    print("Running total is: " + str(startNum))
    end = False

    while (startNum < 21):
        selection = input("type 'a' to select [1-7], type 'b' to select [4-7] ")
        if selection == 'a':
            startNum += randint(1,7)
            print("Total: " + str(startNum))
        if selection == 'b':
            startNum += randint(4,7)
            print("Total: " + str(startNum))
        if selection != 'a' and selection != 'b':
            print("selection not recognized")

        if startNum == 19:
            selection = input("Accept payout of " + str(cash * 1.25) + "? (y/n)")
            if selection == 'y':
                var.yourCash = var.yourCash + cash * 1.25
                var.houseCash = var.houseCash - cash * 1.25
                end = True
                break

        if startNum == 20:
            selection = input("Accept payout of " + str(cash * 1.5) + "? (y/n)")
            if selection == 'y':
                var.yourCash = var.yourCash + cash * 1.5
                var.houseCash = var.houseCash - cash * 1.5
                end = True
                break

    if startNum == 21:
        sleep(1)
        print("Congratulation! Payout: $" + str(cash * 2))
        var.yourCash = var.yourCash + cash * 2
        var.houseCash = var.houseCash - cash * 2
        end = True

    sleep(1)
    print("Winnings: $" + str(var.yourCash))
    print("House: $" + str(var.houseCash))

    if end == True:
        sleep(1)
        selection = input("Play again? (y/n)")
        if selection == 'y':
            cash = input("Enter the amount of cash to play with: ")
            play(int(cash))

    if end == False:
        sleep(1)
        selection = input("You lose. Play again? (y/n)")
        if selection == 'y':
            cash = input("Enter the amount of cash to play with: ")
            play(int(cash))

for i in range (0,100):
    print()
print("The rules are quite simple: don't go over 21.")
print("Each round, you will be given the choice between  option 'a', a random number between 1 and 7,")
print("and option 'b', a random number between 4 and 7. The number is added to your running total,")
print("if your total reaches 19, you have the option to walk away with a small prize!")
print("if your total reaches 20, you have the option to walk away with a slightly larger prize!")
print("if your total reaches 21, you will double your money!")
cash = input("Enter the amount of cash to play with: ")
play(int(cash))
