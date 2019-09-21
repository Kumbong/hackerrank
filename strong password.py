#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"

    count = 0
    if len(set(password).intersection(set(numbers)))==0:
        count+=1
    if len(set(password).intersection(set(lower_case)))==0:
        count+=1
    if len(set(password).intersection(set(upper_case)))==0:
        count+=1
    if len(set(password).intersection(set(special_characters)))==0:
        count+=1
    

    if len(password)+count<6:
        return 6-len(password)

    else:
        return count
                        
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
