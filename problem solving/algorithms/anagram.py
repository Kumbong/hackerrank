#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the anagram function below.
def anagram(s):
    count = 0
    if len(s)%2==1:
        count = -1

    else:
        s1 = list(s[:len(s)//2])
        s2= list(s[len(s)//2:])

        for ch in s1:
            if ch in s2:
                s2.remove(ch)
            else:
                count+=1
    
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
