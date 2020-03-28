#!/bin/python3

import math
import os
import random
import re
import sys
import itertools
# Complete the maximumPerimeterTriangle function below.
def maximumPerimeterTriangle(sticks):
    p_temp = list(set(itertools.permutations(sticks,3)))
    p = []
    for x in p_temp:
        z = sorted(list(x))
        if z[0]+z[1]>z[2]:
            p.append(tuple(sorted(z)))
    p = list(set(p))

    if p:
        if(len(p)>1):
            p.sort(key= lambda x: sum(x))
            return list(p[-1])
        else:
            return list(p[0])
    else:
        return [-1]
 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
