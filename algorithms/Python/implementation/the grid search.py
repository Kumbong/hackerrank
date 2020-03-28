#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gridSearch function below.
def gridSearch(G, P):
    lp,wp,lg,wg = len(P),len(P[0]),len(G),len(G[0])

    for i in range(lg-lp+1):
        if P[0] in G[i]:
            x,start = G[i:i+lp],G[i].index(P[0])
            for j in range(start,wg-wp+1):
                y = [z[j:j+wp] for z in x]
                if y == P:
                    return 'YES'

    return 'NO'
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        RC = input().split()

        R = int(RC[0])

        C = int(RC[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        rc = input().split()

        r = int(rc[0])

        c = int(rc[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P)

        fptr.write(result + '\n')

    fptr.close()
