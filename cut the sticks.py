#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    res = []
    while(len(arr)!=0):
        m = min(arr)
        print(arr)
        print(m)
        res.append(len(arr))
        arr = list(map(lambda x: x-m,arr))

        arr = list(filter(lambda x: x!=0, arr))

    return res



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
