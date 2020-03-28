#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flippingBits function below.
def flippingBits(n):
    return 4294967295-n

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
