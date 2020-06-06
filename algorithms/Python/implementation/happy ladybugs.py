#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the happyLadybugs function below.
def happyLadybugs(b):
    mp = {k:0 for k in set(b)}

    for c in b:
        mp[c]+=1
   
    if '_' not in mp.keys():
        for j in range(1,len(b)):
            if b[j] != b[j-1]:
                if j<len(b)-1 and b[j]!=b[j+1]:
                    return 'NO'
            
    for i, v in mp.items():
        
        if v==1 and i!='_':
            print(i,' ',v)
            return 'NO'

    return 'YES'
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        n = int(input())

        b = input()

        result = happyLadybugs(b)

        fptr.write(result + '\n')

    fptr.close()
