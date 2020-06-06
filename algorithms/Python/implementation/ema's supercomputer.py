#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations
# Complete the twoPluses function below.
def twoPluses(grid):
    pluses = []
    m = len(grid)
    n = len(grid[0])
    for i in range(m):
        for j in range(n):
            for k in range(0,max(m,n)):
                plus = True
                temp = []
                if grid[i][j] == 'G':
                    if i-k>=0 and i+k<m and j-k>=0 and j+k<n:
                        for x in range(i-k,i):
                            temp.append((x,j))
                            if grid[x][j]!='G':
                                plus = False
                        for x in range(j-k,j):
                            temp.append((i,x))
                            if grid[i][x]!='G':
                                plus = False
                        for x in range(i,i+k+1):
                            temp.append((x,j))
                            if grid[x][j]!='G':
                                plus = False
                        for x in range(j,j+k+1):
                            temp.append((i,x))
                            if grid[i][x]!='G':
                                plus = False
         
                        if plus:
                            pluses.append([k,temp])
    print(pluses)
    x = combinations(pluses,2)
  
    a = []

    for p in x:
        if len(set(p[0][1]).intersection(set(p[1][1])))==0:
            a.append((p[0][0]*4+1)*(p[1][0]*4+1))
    a.sort()

    return a[-1]
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = twoPluses(grid)

    fptr.write(str(result) + '\n')

    fptr.close()
