#!/usr/bin/env python3
import sys

def print_wrong() :
    print("\nYou're incorrect. :( ")

print('Magic Time:')
magic_number = int(input("Give me a positive number:\n> "))
if magic_number < 1 :
    print_wrong()
    sys.exit(magic_number)

print('\nRemember this number. It is the magic number.')

minus = int(input("\nWhat's the magic number minus 1?\n> "))
if minus != magic_number - 1 :
    print_wrong()
    sys.exit(magic_number)

plus = int(input("\nWhat's the magic number plus 1?\n> "))
if plus != magic_number + 1 :
    print_wrong()
    sys.exit(magic_number)

multiply = int(input("\nNow, multiply your last two answers together. What do you get?\n> "))
if multiply != (plus * minus) :
    print_wrong()
    sys.exit(magic_number)

plus_one = int(input("\nThen add 1 to your last answer. What do you get?\n> "))
if plus_one != multiply + 1 :
    print_wrong()
    sys.exit(magic_number)

square_root = int(input("\nWhat's the square root of your last answer?\n> "))
if square_root != magic_number :
    print_wrong()
    sys.exit(magic_number)

print('\nI told ya, the number is magic!')
