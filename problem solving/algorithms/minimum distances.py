#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.
def minimumDistances(a):
    m = math.inf
    for i in range(0,len(a)):
        print(a[i])
        for j in range(i+1,len(a)):
            if a[i] == a[j] and abs(j-i) < m :
                m = abs(j-i)

    if m == math.inf:
        m = -1

    return m
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
