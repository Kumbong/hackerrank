#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    arr.sort()

    count = 0
    val= -1
    max_count = 0
    for x in arr:
        if x == val:
            count+=1
        else:
            val = x
            count=1

        if count>max_count:
            max_count = count
            max_val = val

    return max_val
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
