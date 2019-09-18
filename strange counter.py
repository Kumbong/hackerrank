#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the strangeCounter function below.
def strangeCounter(time):

    t = 3
    v = 3

    while  t < time:
        
        v*=2
        t = t+v
      
        if t>=time:
            v = t-time+1

          


    return v
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    result = strangeCounter(t)

    fptr.write(str(result) + '\n')

    fptr.close()
