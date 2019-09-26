#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the counterGame function below.
def counterGame(n):
    player=0
    while(n!=1):
        m = math.floor(math.log(n,2))
        n = n/2 if 2**m==n else n-(2**m)
        if n==1:
            winner = "Louise" if player==0 else "Richard"
          
        player = 1 if player==0 else 0
    return winner

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = counterGame(n)

        fptr.write(result + '\n')

    fptr.close()
