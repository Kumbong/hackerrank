#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the queensAttack function below.
def queensAttack(l, k, r_q, c_q, obstacles):
    n,s,w,e = r_q-1,l-r_q,c_q -1,l-c_q
    nw,ne,sw,se = min(n,w),min(n,e),min(s,w),min(s,e)
    
    for o in obstacles:
        i,j = o[0],o[1]

        if i == r_q:
            if j < c_q:
                w = min(w,c_q-j-1)
            elif j>c_q:
                e = min(e,j-c_q-1)
        elif j == c_q:
            if i<r_q:
                n = min(n,r_q-i-1)
            elif i>r_q:
                s = min(s,i-r_q-1)
        elif abs(i-r_q)==abs(j-c_q):
            if i<r_q and j<c_q:
                nw = min(nw,c_q-j-1)
            elif i<r_q and j>c_q:
                ne = min(ne,j-c_q-1)
            elif i>r_q and j<c_q:
                sw = min(sw,c_q-j-1)
            elif i>r_q and j>c_q:
                se = min(se,j-c_q-1)


    return n+s+w+e+nw+ne+sw+se
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
