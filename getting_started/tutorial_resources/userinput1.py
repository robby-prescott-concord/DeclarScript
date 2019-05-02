#!/usr/bin/env python3
import sys, time
number = int(input("How many seconds should I run my program? : \n"))
print()
for i in range(number) :
    time.sleep(1)
    print("Time: " + str(i + 1) + ' seconds')
    sys.stdout.flush()
