#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    arr.sort()
    minabs = abs(arr[1]-arr[0])

    for i in range(1,len(arr)-1):
        if abs(arr[i]-arr[i+1])<minabs:
            minabs = abs(arr[i]-arr[i+1])

    return minabs
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
