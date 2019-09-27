#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    pairs = 0
    #get a list with all the unique elements in the array

    unique = list(set(ar))

    for el in unique:
        c = ar.count(el)

        pairs+=c//2

    return pairs


    
def count(el,ar):
    #returns the number of occurences of el in an ar

    count = len(filter(lambda x: x==el,ar))

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
