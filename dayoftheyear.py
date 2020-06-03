import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(day,year):
    goal = day
    reach = 0
    months = [31,28,31,30,31,30,31,31,30,31,30,31]
    if year >= 1700:
        if(year%400==0):
            print("leap year!")
            months[1]=29
        elif (year%4 == 0 and year%100 !=0):
            print("leap year!")
            months[1]=29
    if goal < 31:
        return("{}.{}.{}".format(goal,"01",year))
    for i in range(len(months)):
        reach+=months[i]
        if reach+months[i+1] > goal:
            tot = goal-reach
            mon= "0{}".format(i+2) if i+2 < 10 else "{}".format(i+2) 
            return("{}.{}.{}".format(tot,mon,year))

day = int(sys.argv[1])
year = int(sys.argv[2])
progd = dayOfProgrammer(day,year)
print(progd)