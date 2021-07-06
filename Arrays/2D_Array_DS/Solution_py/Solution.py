#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#


def hourglassSum(arr):
    # Write your code here
    resultList = []
    count = 1
    for j in range(0, len(arr[0])):
        for i in range(0, len(arr[1])):
            result = 0
            if i+1 < len(arr[0]) and i+2 < len(arr[0]) and j+1 < len(arr[1]) and j+2 < len(arr[1]):
                one = arr[i][j]
                two = arr[i][j+1]
                three = arr[i][j+2]
                four = arr[i+1][j+1]
                five = arr[i+2][j]
                six = arr[i+2][j+1]
                seven = arr[i+2][j+2]
                # print("#{}: {} {} {}\n      {}  \n    {} {} {}".format(
                #     count, one, two, three, four, five, six, seven))
                result = one + two + three + four + five + six + seven
                resultList.append(result)
                count += 1
    return max(resultList)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
