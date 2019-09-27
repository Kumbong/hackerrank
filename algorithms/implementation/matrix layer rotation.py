#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the matrixRotation function below.
def matrixRotation(matrix, r):
    #get the dimensions of the matrix
    m = len(matrix)
    n = len(matrix[0])

    #get the number of layers of the matrix we will rotate
    layers =  min(m,n)//2

    for i in range(layers):
        #calculate the number of elements in each layer
        num_els = 2*(m-2*i)+2*(n-2*i)-4

        #calculate the number of rotations needed for each layer
        rots = r%num_els

        #flatten the layer and place it in a list
        layer = [matrix[x][i] for x in range(i,i+(m-2*i))]
        layer += [matrix[i+(m-2*i)-1][x] for x in range(i+1,i+(n-2*i)-1)]
        layer += [matrix[x][i+(n-2*i)-1] for x in range(i+(m-2*i)-1,i-1,-1)]
        layer += [matrix[i][x] for x in range(i+(n-2*i)-2,i,-1)]

        #easily r-left rotate the layer
        layer = layer[num_els-rots:]+layer[:num_els-rots]

        #place the rotated elements into the matrix
        for x in  range(i,i+(m-2*i)):   
            matrix[x][i] = layer[0]
            layer = layer[1:]

        for x in range(i+1,i+(n-2*i)-1):
            matrix[i+(m-2*i)-1][x]=layer[0]
            layer = layer[1:]

        for x in range(i+(m-2*i)-1,i-1,-1):
            matrix[x][i+(n-2*i)-1]=layer[0]
            layer = layer[1:]

        for x in range(i+(n-2*i)-2,i,-1):
            matrix[i][x]=layer[0]
            layer = layer[1:]

    #print the matrix
    for i in range(m):
        for j in range(n):
            print(matrix[i][j],end=' ')
        print()
        
if __name__ == '__main__':
    mnr = input().rstrip().split()

    m = int(mnr[0])

    n = int(mnr[1])

    r = int(mnr[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)
