#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the almostSorted function below.
def almostSorted(a):
    aSorted = sorted(a)
    swap = []
    rev  = []
    if aSorted[0]!=a[0]:
        swap.append(0)
    for j in range(1,len(a)):
        if a[j] != aSorted[j]:
            swap.append(j)
        if a[j]<a[j-1]:
       
            rev.append(j-1)
            rev.append(j)

    if len(swap) == 2:
        print('yes')
        print('swap',swap[0]+1,swap[1]+1)
        return
    if len(swap) == 0:
        print('yes')
        return
    for j in range(1,len(rev)):
        if rev[j]- rev[j-1]>1 :
            print('no')
            return
    start = rev[0]
    stop = rev[-1]
    x = a[start:stop+1]
    a = a[:start]+x[::-1]+a[stop+1:]
    if a==aSorted:
        print('yes')
        print('reverse',rev[0]+1,rev[-1]+1)
        return
    print('no')
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    almostSorted(arr)
