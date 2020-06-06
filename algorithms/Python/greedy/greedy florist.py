#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    n = len(c)
    c.sort()
    if k>=n:
        s = sum(c[:k])
    else:
        j,s,tempsum = 1,0,-1
        while tempsum !=0:
            tempsum = sum(c[-k:])*j
            j+=1
            del c[-k:]
            s+=tempsum
    return s


 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
