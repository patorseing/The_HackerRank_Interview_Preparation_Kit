#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#


def sherlockAndAnagrams(s):
    # Write your code here
    # posList = []
    # for i in range(1,len(s)):
    #   for j in range(0,len(s)-i+1):
    #     word = "".join(sorted(s[j:j+i]))
    #     posList.append(word)
    #     print(word)
    # print(posList)

    # count = Counter(posList)
    # print(count)

    # for i in count.values():
    #   print(i, sum(range(i)))

    # return sum(sum(range(i)) for i in count.values())

    count = Counter(("".join(sorted(s[j:j+i]))
                     for i in range(1, len(s)) for j in range(0, len(s)-i+1)))
    return sum(sum(range(i)) for i in count.values())
    # https://www.thepoorcoder.com/hackerrank-sherlock-and-anagrams-solution/


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
