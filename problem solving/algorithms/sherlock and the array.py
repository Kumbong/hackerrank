#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the balancedSums function below.
def balancedSums(arr):

    first = 0
    last = len(arr)-1
    found = False
    while( first<=last and not found):
        mid = (first + last)//2
        ls = left_sum(arr,mid) 
        rs = right_sum(arr,mid)
        if ls == rs:
            found = True
        else:
            if ls > rs:
                last = mid - 1
            else:
                first = mid + 1    
    
    if found:
        return 'YES'
    
    else:
        return 'NO'

def left_sum(arr,i):
    return 0 + sum(arr[:i])

def right_sum(arr,i):
    return 0 + sum(arr[i+1:])
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()
