#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isValid function below.
def isValid(s):
    ss = list(set(s))
    fs = []
    for c in ss:
        fs.append(s.count(c))
    

    if (len(list(set(fs))))==1:
        return 'YES'
    elif len(list(set(fs)))==2:
        mx= max(fs)
        mi= min(fs)

        if (fs.count(mx) ==1 or fs.count(mi)==1) and (mx-mi == 1):
            return 'YES'
        elif fs.count(mi)==1 and mi==1:
            return 'YES'
    return 'NO'
            

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
