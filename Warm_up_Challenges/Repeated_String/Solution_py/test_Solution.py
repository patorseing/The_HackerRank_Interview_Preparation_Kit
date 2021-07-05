import unittest
import Solution


class SolveTestCase(unittest.TestCase):
    def testCaseI(self):
        s = "aba"
        n = 10
        actual = Solution.repeatedString(s, n)
        excepted = 7
        self.assertEqual(actual, excepted)

    def testCaseII(self):
        s = "a"
        n = 1000000000000
        actual = Solution.repeatedString(s, n)
        excepted = 1000000000000
        self.assertEqual(actual, excepted)
