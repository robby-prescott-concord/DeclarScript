#!/usr/bin/env python3
import  time
number = int(input("How many seconds should I run my program? : "))
for i in range(number) :
    time.sleep(1)
    print("Time: " + str(i + 1) + ' seconds')
