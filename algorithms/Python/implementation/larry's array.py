#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the larrysArray function below.
def larrysArray(a):
    aSorted = sorted(a)
    while(a[:len(a)-2]!=aSorted[:len(a)-2]):
        for i in range(len(a)-2):
            minIndex = a[i:i+3].index(min(a[i:i+3]))
            x = a[i:i+3][minIndex:]+a[i:i+3][:minIndex]
            a[i:i+3] = x
    if a[len(a)-2:] != aSorted[len(a)-2:]:
        return 'NO'
    else:
        return 'YES'
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        A = list(map(int, input().rstrip().split()))

        result = larrysArray(A)

        fptr.write(result + '\n')

    fptr.close()
