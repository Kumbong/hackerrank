#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makingAnagrams function below.
def makingAnagrams(s1, s2):

    sbig =list(s1)
    ssmall = list(s2)
        
    for c in s1:
        if c in ssmall:
            ssmall.remove(c) 
            sbig.remove(c)

    return len(ssmall)+len(sbig)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
