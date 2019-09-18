#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the funnyString function below.
def funnyString(s):
    rs = s[::-1]

    print(rs)
    scount=0
    rscount=0
    for i in range(len(s)-1):
        scount=abs(ord(s[i+1])-ord(s[i]))
        rscount=abs(ord(rs[i+1])-ord(rs[i]))

        if scount!=rscount:
            return "Not Funny"

   
    return "Funny"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
