#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cavityMap function below.
def cavityMap(grid):
    n = len(grid)
    new_grid=[]
    print(new_grid)
    for i in range(n):
        temp =""
        for j in range(n):
            if i!=0 and j!=0 and i!=n-1 and j!=n-1:
                if int(grid[i][j])>int(grid[i-1][j]) and int(grid[i][j])>int(grid[i+1][j]) and int(grid[i][j])>int(grid[i][j-1]) and int(grid[i][j])>int(grid[i][j+1]):
                    temp+='X'
                else:
                    temp+=str(grid[i][j])
            else:
                temp+=str(grid[i][j])

        new_grid.append(temp)
    return new_grid
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
