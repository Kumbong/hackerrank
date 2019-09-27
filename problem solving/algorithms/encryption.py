#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    s.strip()
    ''.join(s.split(' '))
    
    L = len(s)
    r = math.floor(math.sqrt(L))
    c = math.ceil(math.sqrt(L))

    if r*c < L :
        r=c
    s2=""
    for j in range(c):
        s1=""
        for i in range(r):
            if j+c*i<L:
                s1+=s[j+c*i]
        s2+=s1+" "

    return s2



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
