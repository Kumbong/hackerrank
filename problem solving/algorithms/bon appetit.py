#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    sum = 0
    for i in bill:
        sum+=i
    sum = sum - bill[k]
    if sum//2 == b:
        print('Bon Appetit')
    else:
        print(b-(sum//2))

if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
