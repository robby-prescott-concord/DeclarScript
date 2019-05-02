#!/usr/bin/env python3
import sys

def printDead() :
    print("Hmm... that's too bad. :( ")

answer = input("Are you alive? (Y or N)\n")
if answer != 'Y' and answer != 'y' :
    printDead()
    sys.exit(17)

answer = input("Are you sure? (Y or N)\n")
if answer != 'Y' and answer != 'y' :
    printDead()
    sys.exit(17)

answer = int(input("How sure are you? (%)\n"))
if answer != 100 :
    printDead()
    sys.exit(17)

answer = input("Okay. So you're not not dead then? (Y or N)\n")
if answer != 'N' and answer != 'n' :
    printDead()
    sys.exit(17)

answer = input("Wait... So you're not living then, right? (Y or N)\n")
if answer != 'N' and answer != 'n' :
    printDead()
    sys.exit(17)

answer = int(input("How many feet are you NOT buried underground then? (ft)\n"))
if answer != 6 :
    printDead()
    sys.exit(17)

answer = input("So, we have concluded that you are indeed alive? (Y or N)\n")
if answer != 'Y' and answer != 'y' :
    printDead()
    sys.exit(17)

answer = input("And you're not sure about this then? (Y or N)\n")
if answer != 'N' and answer != 'n' :
    printDead()
    sys.exit(17)

answer = input("Okay... you can continue if you guess my favorite color. (color-lowercase)\n")
if answer != 'purple' :
    printDead()
    print('It\'s actually purple')
    sys.exit(17)

answer = int(input("...And my favorite number too actually. (number)\n"))
if answer != 17 :
    printDead()
    print('Favorite numbers, Return Codes, what\'s the difference...')
    sys.exit(17)

print('Well Done, you may continue...')
