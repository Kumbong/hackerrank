#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    apples = list(map(lambda x: x+a,apples))

    oranges =list(map(lambda x: x+b, oranges))
 

    apples = list(filter(lambda x: x>=s and x<=t,apples))

    oranges = list(filter(lambda x: x>=s and x<=t,oranges))


    print(len(apples))
    print(len(oranges))

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
