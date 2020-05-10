#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumLoss function below.
def minimumLoss(price):
    sprice = sorted(price,reverse=True)
    print(sprice)
    m = sprice[0]-sprice[-1]

    for j in range(0,len(sprice)-1):
        if sprice[j]-sprice[j+1]<m:
            if price.index(sprice[j])<price.index(sprice[j+1]):
                m = sprice[j]-sprice[j+1]
    return m
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    price = list(map(int, input().rstrip().split()))

    result = minimumLoss(price)

    fptr.write(str(result) + '\n')

    fptr.close()
