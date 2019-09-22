#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    ldsum = 0
    rdsum=0

    n = len(arr)
    
    for i in range(0,n):
        ldsum+= arr[i][n-1-i]
        rdsum+= arr[i][i]

    return abs(rdsum-ldsum)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
