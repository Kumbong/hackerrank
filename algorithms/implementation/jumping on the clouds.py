#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(a):

    c = 0
    i = 0
    while i < n - 1:
        if i + 2 >= n or a[i + 2] == 1:   
            i +=1
            c+=1
        else:
            i +=2
            c+=1

    return c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
