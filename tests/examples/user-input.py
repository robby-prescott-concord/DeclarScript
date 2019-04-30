#!/usr/bin/env python3
import sys, os


# asking for user input & casting to int
number = float(input("Give me a number: "))
sum = number + 10
print('...plus 10! -> ' + str(sum))

#try catch block
try:
    number_2 = int(input("\nAnother something please: "))
    result = number_2 * 3
    print('...tripled! -> ' + str(result))
except Exception:
    print("I meant another Integer...")
    sys.exit(1)
    pass

print('my favorite color is green!')
sys.exit(3)
