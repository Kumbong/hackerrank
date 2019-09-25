#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kaprekarNumbers function below.
def kaprekarNumbers(p, q):
    found = False
    for n in range(p,q+1):
        d = len(str(n))
        s = n*n
        ds = len(str(s))
        l=str(s)[:ds-d]
        r=str(s)[ds-d:]

        if l and int(l)+int(r)==n:
            found = True
            print(n,end=' ')

        elif not l and n==1:
            found  = True
            print(n,end=" ")

    if not found:
        print("INVALID RANGE")

if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)
