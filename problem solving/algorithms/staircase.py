#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    for i in range(0,n+1):
        if(i!=0):
            for j in range(0,n-i):
                print(' ',end='')
            for k in range(0,i):
                print('#',end='')
            print('')
if __name__ == '__main__':
    n = int(input())

    staircase(n)
