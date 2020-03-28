#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the timeInWords function below.
def timeInWords(h, m):
    t = ["zero","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen", "fourteen", "fifteen","sixteen","seventeen", "eighteen","nineteen","twenty","twenty one","twenty two","twenty three","twenty four","twenty five","twenty six","twenty seven","twenty eight","twenty nine"]
    if m==0:
        return t[h]+" o' clock"
    
    elif m==30:
        return "half past "+t[h]
    
    elif m==15:
        return "quarter past "+t[h]

    elif m==45:
        return "quarter to "+t[(h%12 +1)]

    elif m>1 and m<30 and m!=15:
        return t[m]+" minutes past "+t[h]

    elif m==1:
        return t[m]+" minute past "+t[h]

    elif m>30 and m!=45:
        return t[60-m]+" minutes to "+t[(h+1)%12]
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
