#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the candies function below.
def candies(n, arr):
    left = [1]*n
    right = [1]*n
    s = 0
    for j in range(1,n):
        if arr[j]>arr[j-1]:
            left[j] = left[j-1]+1
        if arr[n-j-1]>arr[n-j]:
            right[n-j-1] = right[n-j]+1

    for j in range(n):
        s+=max(left[j],right[j])

    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = candies(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
