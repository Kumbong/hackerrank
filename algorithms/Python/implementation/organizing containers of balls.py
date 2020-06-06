#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the organizingContainers function below.
def organizingContainers(container):
    for i in range(len(container)):
        rowSum = [sum(container[i]) for i in range(len(container))]
        colSum = [sum(x) for x in zip(*container)]

    print(rowSum)
    print(colSum)
    if sorted(rowSum) != sorted(colSum):
        return 'Impossible'
    return 'Possible'
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()
