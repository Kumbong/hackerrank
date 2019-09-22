#!/bin/python3

import os
import sys
from math import floor

#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):
    rounded =[]
    for grade in grades:
        if grade<38:
            rounded.append(grade)
        else:
            if (floor((grade//5)*5+5) -grade) < 3:
                grade = floor((grade//5)*5+5)
            rounded.append(grade)

    for grade in rounded:
        print(grade)
    return rounded

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()
