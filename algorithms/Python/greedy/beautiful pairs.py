#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulPairs function below.
def beautifulPairs(A, B):

    flag = False
    count = 0
    for i in range(len(A)):
        flag = False
        print(B)
        for j in range(len(B)):
            if A[i]==B[j]:
                flag = True
                count+=1
                break
        if flag:
            del B[j]
        
    if (count == len(A)):
        return count-1
    else:
        return count+1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    A = list(map(int, input().rstrip().split()))

    B = list(map(int, input().rstrip().split()))

    result = beautifulPairs(A, B)

    fptr.write(str(result) + '\n')

    fptr.close()
