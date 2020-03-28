#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubarray function below.
def maxSubarray(arr):
    #maximum subsequence is simply the sum of all positive numbers
    #in the array if there are any positive numbers
    max_ss= sum(list(filter(lambda x: x>0,arr)))

    #or its the largest number in the array if there is none
    if not max_ss:
        max_ss = max(arr)


    max_sa=arr[0] #max for subarray
    local_max = 0

    #straightforward application of kadane's algorithm..
    for i in range(len(arr)):
        local_max = max(local_max+arr[i],arr[i])

        if local_max>max_sa:
            max_sa = local_max

    return [max_sa,max_ss]
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = maxSubarray(arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
