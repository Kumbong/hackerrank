#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    min = scores[0]
    max = scores[0]
    
    c1 =0
    c2 =0
    for score in scores:
        if score > max:
            max = score
            c1+=1
        elif score<min:
            min = score
            c2+=1

    return [c1,c2]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
