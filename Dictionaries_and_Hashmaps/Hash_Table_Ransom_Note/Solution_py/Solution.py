#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#


def countWord(WordList):
    wordDict = dict()
    for x in WordList:
        try:
            wordDict[x] += 1
        except:
            wordDict[x] = 0
    return wordDict


def checkMagazine(magazine, note):
    # Write your code here
    magDict = countWord(magazine)
    noteDict = countWord(note)

    try:
        return "No" if False in list(magDict[x] >= noteDict[x] for x in note) else "Yes"
    except:
        return "No"


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    print(checkMagazine(magazine, note))
