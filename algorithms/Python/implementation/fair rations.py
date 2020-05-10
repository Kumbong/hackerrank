#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the fairRations function below.
def fairRations(B):
    last_odd_num_index = -1
    sumB = 0
    count  = 0
    for i in range(len(B)):
        sumB+=B[i]
        if B[i]%2==1:
            if last_odd_num_index == -1:
                last_odd_num_index = i
            else:
                count+=(i-last_odd_num_index)*2
                last_odd_num_index = -1
    if sumB%2==1:
        return 'NO'
    else:
        return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input())

    B = list(map(int, input().rstrip().split()))

    result = fairRations(B)

    fptr.write(str(result) + '\n')

    fptr.close()
