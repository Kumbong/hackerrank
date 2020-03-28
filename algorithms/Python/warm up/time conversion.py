#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    t = s[0:8]
    r = s[8:10]
    
    r = r.lower()
    if r=='pm':
        sum = int(t[0:2])+12

        if sum ==24:
            #if(int(s[3:5])!=0 or int(s[6:8])!=0):
            t= '00'+s[2:8]
        
        t= str(int(t[0:2])+12)+s[2:8]
    if r =='am' and s[0:2] == '12':
        t= '00'+s[2:8]
    return t


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
