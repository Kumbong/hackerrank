#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superReducedString function below.
def superReducedString(s):

    stk =[]

    for c in s:
        if stk and stk[-1]==c:
            stk.pop()

        else:
            stk.append(c)

    if stk:
        return ''.join(stk)
    else:
        return 'Empty String'
            


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
