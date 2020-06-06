#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the connectedCell function below.
def connectedCell(matrix):
    cells = []
    m = 0
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]==1:
                cells.append((i,j))
   
    for cell in cells:
        temp = [cell]
        notFound = []
        for c in cells:
            for t in temp:
                tFound = False
                if (abs(c[0]-t[0])<=1 and abs(c[1]-t[1])<=1):
                    tFound = True
                if tFound:
                    if c not in temp:
                        temp.append(c)
                else:
                    notFound.append(c)
        for c in notFound:
            for t in temp:
                tFound = False
                if (abs(c[0]-t[0])<=1 and abs(c[1]-t[1])<=1):
                    tFound = True
                if tFound:
                    if c not in temp:
                        temp.append(c)
           
        if len(temp)>m:
            m = len(temp)
    return m
                    
                    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    m = int(input())

    matrix = []

    for _ in range(n):
        matrix.append(list(map(int, input().rstrip().split())))

    result = connectedCell(matrix)

    fptr.write(str(result) + '\n')

    fptr.close()
