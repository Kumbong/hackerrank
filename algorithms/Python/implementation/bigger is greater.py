#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the biggerIsGreater function below.
def biggerIsGreater(w):
    w = list(w)
    i = len(w)-1

    while i >0 and w[i-1]>=w[i]:
        i-=1
    if i<=0:
        return 'no answer'

    j = len(w)-1
    while w[j]<=w[i-1]:
        j-=1
    w[i-1],w[j] = w[j],w[i-1]
    w[i:] = w[len(w)-1:i-1:-1]

    return ''.join(w)

    j = len(w)-1
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
