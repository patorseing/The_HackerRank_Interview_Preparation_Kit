#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#


def step(form):
    '''
    def step(start, form, count, reverse=True):
    swap like Question is not work
    '''
    # countForEach = 0
    # if reverse:
    #     s = list(reversed(range(len(start))))
    #     swapIndex = -1
    # else:
    #     s = list(range(len(start)))
    #     swapIndex = 1
    # for i in s:
    #     if start[i] != form[i]:
    #         countForEach += 1
    #         # print(start, form, start[i],
    #         #       start[i+swapIndex], reverse, countForEach, count)
    #         temp = start[i]
    #         start[i] = start[i+swapIndex]
    #         start[i+swapIndex] = temp
    #     elif countForEach > 0:
    #         break
    # if countForEach > 2:
    #     return "Too chaotic"
    # count += countForEach
    # if start == form:
    #     return count
    # return step(start, form, count, not reverse)
    '''
    reverse step back to origin
    eg
    2 1 5 3 4 -> 1 2 3 4 5
    1 0 4 2 3
      i  P
    # 0, 1: range(0, 0)
    # 1, 0: range(0, 1)
    #   0 -> Q[0] = 2 > 0 T +1
    # 2, 4: range(3, 2)
    # 3, 2: range(1, 3)
    #   1 -> Q[1] = 1 > 2 F
    #   2 -> Q[2] = 5 > 2 T +1
    # 4, 3: range(2, 4)
    #   2 -> Q[2] = 5 > 3 T +1
    #   3 -> Q[3] = 3 > 3 F
    # RESULT = 3
    how many step to move back and comply each together
    '''
    moves = 0
    Q = [P-1 for P in form]
    for i, P in enumerate(Q):
        if P - i > 2:
            return "Too chaotic"
        for j in range(max(P-1, 0), i):
            if Q[j] > P:
                moves += 1
    return moves


def minimumBribes(q):
    # Write your code here
    start = sorted(q)
    print(step(start, q, 0))


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
