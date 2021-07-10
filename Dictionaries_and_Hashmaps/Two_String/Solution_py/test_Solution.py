import unittest
import Solution


class SolveTestCase(unittest.TestCase):
    def testCaseI(self):
        s1 = "hello"
        s2 = "world"
        actual = Solution.twoStrings(s1, s2)
        excepted = "YES"
        self.assertEqual(actual, excepted)

    def testCaseII(self):
        s1 = "hi"
        s2 = "world"
        actual = Solution.twoStrings(s1, s2)
        excepted = "NO"
        self.assertEqual(actual, excepted)
