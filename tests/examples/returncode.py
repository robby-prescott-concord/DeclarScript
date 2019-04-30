#!/usr/bin/env python3
import sys, os

answer = 0
number = 0
while answer != 1 :
    number = int(input("Enter a return code: "))
    print('Are you sure about ' + str(number) + '?')
    answer = int(input("Type 0 or 1. 0 = no, 1 = yes : "))
sys.exit(number)
