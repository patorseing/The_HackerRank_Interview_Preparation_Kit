import unittest
import Solution


class SolveTestCase(unittest.TestCase):
    def testCaseI(self):
        d = 1
        a = [1, 2, 3, 4, 5]
        actual = Solution.rotLeft(a, d)
        excepted = [2, 3, 4, 5, 1]
        self.assertEqual(actual, excepted)

    def testCaseII(self):
        d = 2
        a = [1, 2, 3, 4, 5]
        actual = Solution.rotLeft(a, d)
        excepted = [3, 4, 5, 1, 2]
        self.assertEqual(actual, excepted)

    def testCaseIII(self):
        d = 3
        a = [1, 2, 3, 4, 5]
        actual = Solution.rotLeft(a, d)
        excepted = [4, 5, 1, 2, 3]
        self.assertEqual(actual, excepted)

    def testCaseIV(self):
        d = 4
        a = [1, 2, 3, 4, 5]
        actual = Solution.rotLeft(a, d)
        excepted = [5, 1, 2, 3, 4]
        self.assertEqual(actual, excepted)
