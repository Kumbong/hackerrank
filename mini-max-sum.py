#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    sum = 0

    for num in arr:
        sum+=num

    max = sum - arr[0]
    min = sum -arr[0]

    for num in arr:
        diff = sum -num

        if diff > max:
            max = diff
        elif diff<min:
            min = diff

    print(min,end=' ')
    print(max,end=' ')
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
