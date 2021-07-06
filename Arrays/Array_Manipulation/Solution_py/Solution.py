#!/bin/python3

import math
import os
import random
import re
import sys
import numpy as np

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#


def processStepHalf(q, n):
    a, b, k = q
    arr = [0] * n
    start = a - 1
    if q != [0, 0, 0]:
        if start < 0:
            start = 0
        arr = arr[:start] + [k] * (b-a+1) + arr[b:]
    return arr


def arrayManipulation(n, queries):
    # Write your code here
    # step = [0] * n
    # for a, b, k in queries:
    #     for i in range(a-1, b):
    #         step[i] += k
    arr = [0] * (n+1)
    # add the value at first index
    # subtract the value at last index + 1
    for q in queries:
        start, end, amt = q
        arr[start-1] += amt
        arr[end] -= amt

    # max value and running sum
    mv = -1
    running = 0
    for a in arr:
        running += a
        if running > mv:
            mv = running

    return mv


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
