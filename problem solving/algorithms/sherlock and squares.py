#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the squares function below.
def squares(a, b):
    
    upper = 0
    lower = 0
    for x in range(a,b+1):
        if math.sqrt(x).is_integer():
            lower = int(math.sqrt(x))
            break

    for x in range(b,a-1,-1):
        if math.sqrt(x).is_integer():
            upper = int(math.sqrt(x))
            break

    if upper == 0 and lower==0:
        return 0

    else:
        return (upper-lower)+1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
