#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#


def repeatedString(s, n):
    # Write your code here
    countA = 0
    for string in s:
        if string == 'a':
            countA += 1
    newCountA = math.floor(n/len(s)) * countA
    if n % len(s) == 0:
        return newCountA

    for i in range(n % len(s)):
        if s[i] == 'a':
            newCountA += 1
    return newCountA


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
