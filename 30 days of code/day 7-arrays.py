#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    rev = []
    for i in range(n-1,-1,-1):
        rev.append(str(arr[i]))

    print(' '.join(rev))
    
