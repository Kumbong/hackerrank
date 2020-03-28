#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def reverse_number(n):
    rev=0
    while(n>0):
        dig=n%10
        rev=rev*10+dig
        n=n//10
    
    return rev

def beautifulDays(i, j, k):

    bd = 0
    for x in range(i,j+1):
        if abs(x-reverse_number(x))%k==0:
            bd+=1

    return bd

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
