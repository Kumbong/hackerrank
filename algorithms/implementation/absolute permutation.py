#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the absolutePermutation function below.
def absolutePermutation(n, k):
    permutation = [ ] #permutation to return

    #used[i] is False if i+1 has not been added to permuation already and
    #it is True if otherwise
    used = [False]*n

    for i in range(1,n+1):
        t1,t2 = i-k,i+k 

        #we can either use i-k or i+k  just keep track of which is within the
        #desired range
        ops = []
        if t1>=1:
            ops.append(t1)
        if t2<=n:
            ops.append(t2)

        #if none is within desired range we can have an absolute permutation
        if not ops:
            permutation =  [-1]
            break
        
        #try to use the minimum of the two options depending on which is free
        if not used[min(ops)-1]:
            permutation.append(min(ops))
            used[min(ops)-1] = True
        elif not used[max(ops)-1]:
            permutation.append(max(ops))
            used[max(ops)-1] = True
        else:
            return [-1]
            break

    return permutation


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        result = absolutePermutation(n, k)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
