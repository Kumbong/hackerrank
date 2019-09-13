#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the closestNumbers function below.
def closestNumbers(arr):
    arr.sort()

    min_diff = math.inf
    mins = []
    for i in range(len(arr)-1):
        if abs(arr[i]-arr[i+1])<min_diff:
            min_diff = abs(arr[i]-arr[i+1])
            mins =[arr[i],arr[i+1]]
        elif abs(arr[i]-arr[i+1])==min_diff:
            mins.append(arr[i])
            mins.append(arr[i+1])

    return mins
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
