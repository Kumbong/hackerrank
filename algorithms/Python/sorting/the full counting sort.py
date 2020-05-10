#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSort function below.
def countSort(arr):
    x = [[] for _ in range(100)]
    for i in range(len(arr)//2):
        x[int(arr[i][0])].append('-')
    for i in range(len(arr)//2,len(arr)):
        x[int(arr[i][0])].append(arr[i][1])
    s = ''
    for el in x:
        for c in el:
            s+=c+' '
    print(s)
if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
