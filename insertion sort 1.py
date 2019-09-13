#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
    x = arr[-1]

    end = len(arr) - 1

    for j in range(end-1,-1,-1):
        if arr[j]>x:
            arr[j+1]=arr[j]
            print(*arr,sep=" ")

            if j==0:
                arr[j]=x
                print(*arr,sep=" ")

        else:
            arr[j+1]=x
            print(*arr,sep=" ")
            break

           
        

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
