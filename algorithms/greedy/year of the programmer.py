#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):

    if year>=1700 and year<=1917:#julian calendar
        if year%4==0:
            date = "12.09."+str(year)
        else:
            date = "13.09."+str(year)

    elif year>1918:
        if (year%400==0) or (year%4==0 and year%100!=0):
            date = "12.09."+str(year)
        else:
            date = "13.09."+str(year)

    elif year==1918:
         date = "26.09.1918"

    return date

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
