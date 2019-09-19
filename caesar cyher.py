#!/bin/python3

import math
import os
import random
import re
import sys
import string

# Complete the caesarCipher function below.
def caesarCipher(s, k):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    sc=""
   
    for c in s:
        u = False
        if c.isalpha():
            if c.isupper():
                u =True
                c = c.lower()
            ch = alphabet[(alphabet.index(c)+k)%(len(alphabet))]
            if u:
                ch = ch.upper()
            sc+=ch
        else:
            sc+=c

    return sc



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    k = int(input())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
