#!/bin/python3

import os
import sys

#
# Complete the getTotalX function below.
#
def getTotalX(a, b):
    a.sort()
    b.sort()

    min = a[len(a)-1]
    max = b[0]

    count =0

    for i in range(min,max+1):
        for x in a:
            if i%x !=0:
                break
        else:
            for y in b:
                if y%i != 0:
                    break
            else:
                count+=1
    
    print(count)
    return count



if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    total = getTotalX(a, b)

    f.write(str(total) + '\n')

    f.close()
