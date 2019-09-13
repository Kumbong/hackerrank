#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort2 function below.
def insertionSort2(n, arr):
    for j in range(1,n):
        unsorted = arr[:j+1]
        sorted = insertionSort1(unsorted)
        arr[:j+1] = sorted
        print(*arr,sep=" ")

def insertionSort1(arr):
    x = arr[-1]

    end = len(arr) - 1

    for j in range(end-1,-1,-1):
        if arr[j]>x:
            arr[j+1]=arr[j]
  

            if j==0:
                arr[j]=x

        else:
            arr[j+1]=x

            break

    return arr   
        

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
