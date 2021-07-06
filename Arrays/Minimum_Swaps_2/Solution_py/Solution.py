#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.

def minimumSwaps(arr, count=0):
    form = sorted(arr)
    for i, P in enumerate(arr):
        if P-1 != i:
            temp = arr[P-1]
            arr[P-1] = arr[i]
            arr[i] = temp
            count += 1
    if arr == form:
        return count
    return minimumSwaps(arr, count)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
