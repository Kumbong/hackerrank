import math
import os
import random
import re
import sys

# Complete the largestPermutation function below.
def largestPermutation(k, arr):
    n = len(arr)
    i = 0 
    c = 0
    if k>n:
        return sorted(arr,reverse=True)

    indices = {}
    for j in range(n):
        indices[arr[j]] = j
    
    print(indices)
    while(c<k and i<n-1):
        if arr[i]!=n-i:
            temp,j = arr[i],indices[n-i]
            arr[i],arr[j] = arr[j],temp
            indices[temp] = j
            c+=1
        i+=1

    return arr
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = largestPermutation(k, arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()


    
