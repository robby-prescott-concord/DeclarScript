#!/usr/bin/env python3
import sys, os, time


# asking for user input & casting to int
number = int(input("How many seconds should I run my program? : "))
for i in range(number) :
    print("Time: " + str(i))
    time.sleep(1)
print("Time: " + str(number))
print("COMPLETE")
