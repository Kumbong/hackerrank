#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the surfaceArea function below.
def surfaceArea(A):
    area = 0

    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j]!= 0:
                area+=2
                if i-1>=0 and A[i-1][j]!=0:
                    if A[i][j]>A[i-1][j]:
                        area+=A[i][j]-A[i-1][j]
                else:
                    area+=A[i][j]
                if i+1<len(A) and A[i+1][j]!=0:
                    if A[i][j]>A[i+1][j]:
                        area+=A[i][j]-A[i+1][j]
                else:
                    area+=A[i][j]
                if j-1>=0 and A[i][j-1]!=0:
                    if A[i][j]>A[i][j-1]:
                        area+=A[i][j]-A[i][j-1]
                else:
                    area+=A[i][j]
                if j+1<len(A[0]) and A[i][j+1]!=0:
                    if A[i][j]>A[i][j+1]:
                        area+=A[i][j]-A[i][j+1]
                else:
                    area+=A[i][j]

    return area
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    HW = input().split()

    H = int(HW[0])

    W = int(HW[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    fptr.write(str(result) + '\n')

    fptr.close()
