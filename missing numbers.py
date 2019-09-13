#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the missingNumbers function below.
def missingNumbers(arr, brr):

   #get all the unique elements in the second list
    unique = list(set(brr))

    missing = [] #holds the missing elements from the first list

    for el in unique:
        if (brr.count(el)>arr.count(el)): #if the count in the second array exceeds
        #that in the first list then the element is missing
        
            missing.append(el)

    missing.sort()

    return missing

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    m = int(input())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
