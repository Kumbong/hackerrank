#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    ranks =[]
    scores = sorted(list(set(scores)),reverse=True)
    n = len(scores)
    start = n-1
    for sc in alice:
        pos_found = False
        for i in range(start,-1,-1):
            if scores[i]>sc:
                ranks.append(i+2)
                pos_found =True
                break
            if i==0 and pos_found == False:
                ranks.append(1)

        start = i
    return ranks

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
