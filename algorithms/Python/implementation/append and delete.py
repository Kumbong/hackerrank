#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
 
    #assume both at least one string is a substring of the other 
    j = min(len(s),len(t))
    for i in range(min(len(t),len(s))):
        if s[i]!=t[i]:
            j = i

    moves = len(s)-j+len(t)-j

    if moves>k:
        return 'No'

    else:
        if moves<k and (k-moves)%2:
            if (k-moves)>=j*2:
                return 'Yes'
            else:
                return 'No'
        return 'Yes'


    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
