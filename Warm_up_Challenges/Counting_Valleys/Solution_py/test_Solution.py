import unittest
import Solution


class SolveTestCase(unittest.TestCase):
    def testCaseI(self):
        steps = 8
        path = "UDDDUDUU"
        actual = Solution.countingValleys(steps, path)
        excepted = 1
        self.assertEqual(actual, excepted)

    def testCaseII(self):
        steps = 12
        path = "DDUUDDUDUUUD"
        actual = Solution.countingValleys(steps, path)
        excepted = 2
        self.assertEqual(actual, excepted)

    def testCaseIII(self):
        steps = 10
        path = "UDUUUDUDDD"
        actual = Solution.countingValleys(steps, path)
        excepted = 0
        self.assertEqual(actual, excepted)

    def testCaseIV(self):
        steps = 10
        path = "DUDDDUUDUU"
        actual = Solution.countingValleys(steps, path)
        excepted = 2
        self.assertEqual(actual, excepted)
