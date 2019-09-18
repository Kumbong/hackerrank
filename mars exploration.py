#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the marsExploration function below.
def marsExploration(s):
    mul = (len(s)//3)

    ref_str = "SOS"*mul

    diff = [i for i in range(len(s)) if s[i]!=ref_str[i]]

    return len(diff)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
