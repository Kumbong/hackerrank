#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the decentNumber function below.
def decentNumber(a):
    b = a
    while(b%3!=0):
        b -= 5
    if(b<0):
        print(-1)
    else:
        print(b*'5'+(a-b)*'3')

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        decentNumber(n)
