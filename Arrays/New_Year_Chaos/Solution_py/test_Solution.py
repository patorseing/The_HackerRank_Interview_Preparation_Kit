import unittest
import Solution


class SolveTestCase(unittest.TestCase):
    def testCaseI(self):
        q = [2, 1, 5, 3, 4]
        start = sorted(q)
        actual = Solution.step(start, q, 0)
        excepted = 3
        self.assertEqual(actual, excepted)

    def testCaseII(self):
        q = [2, 5, 1, 3, 4]
        start = sorted(q)
        actual = Solution.step(start, q, 0)
        excepted = "Too chaotic"
        self.assertEqual(actual, excepted)

    def testCaseIII(self):
        q = [1, 2, 3, 5, 4, 6, 7, 8]
        start = sorted(q)
        actual = Solution.step(start, q, 0)
        excepted = 1
        self.assertEqual(actual, excepted)

    def testCaseIV(self):
        q = [4, 1, 2, 3]
        start = sorted(q)
        actual = Solution.step(start, q, 0)
        excepted = "Too chaotic"
        self.assertEqual(actual, excepted)

    def testCaseV(self):
        q = [5, 1, 2, 3, 7, 8, 6, 4]
        start = sorted(q)
        actual = Solution.step(start, q, 0)
        excepted = "Too chaotic"
        self.assertEqual(actual, excepted)

    def testCaseVI(self):
        q = [1, 2, 5, 3, 7, 8, 6, 4]
        start = sorted(q)
        actual = Solution.step(start, q, 0)
        excepted = 7
        self.assertEqual(actual, excepted)

    def testCaseVII(self):
        q = [1, 2, 5, 3, 4, 7, 8, 6]
        start = sorted(q)
        actual = Solution.step(start, q, 0)
        excepted = 4
        self.assertEqual(actual, excepted)
