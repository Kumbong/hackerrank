#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingSort function below.
def countingSort(arr):
    c = [0]*(max(arr)+1)


    for x in arr:
        c[x]+=1

    ls = []

    for x in range(len(c)):
        for i in range(c[x]):
            ls.append(x)

    return ls
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
