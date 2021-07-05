import unittest
import Solution
import sys


class SolveTestCase(unittest.TestCase):
    def testCaseI(self):
        c = [0, 0, 1, 0, 0, 1, 0]
        actual = Solution.jumpingOnClouds(c)
        excepted = 4
        self.assertEqual(actual, excepted)

    def testCaseII(self):
        c = [0, 0, 0, 0, 1, 0]
        actual = Solution.jumpingOnClouds(c)
        excepted = 3
        self.assertEqual(actual, excepted)

    def testCaseIII(self):
        c = list(map(int, "0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 0 1 0 1 0 0 0 1 0 0 1 0 0 0 1 0 1 0 0 0 0 0 0 0 0 1 0 0 1 0 1 0 0".split()))
        actual = Solution.jumpingOnClouds(c)
        excepted = 28
        self.assertEqual(actual, excepted)
