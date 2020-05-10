#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pylons function below.
def pylons(k, arr):
    cities = []

    for i in range(len(arr)):
        if not cities or not abs(i-cities[-1])<k:
            city = -1
            for j in range(i-k+1,min(i+k,len(arr))):
                if arr[j]==1:
                    city = j
            if city != -1:
                cities.append(city)           
            else:
                print(arr[i])
                print(arr[i-k:i])
                print(arr[i:])
                return -1
    return len(cities)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pylons(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
