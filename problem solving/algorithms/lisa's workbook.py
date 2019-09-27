#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the workbook function below.
def workbook(n, k, arr):
    page = 1
    count =0
    for i in range(n):
        q = arr[i]

        j = 1
        while(j<=q):
            if j==page:
                count+=1
            if(j%k==0) or j==q:
                page+=1

            j+=1
           

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()

