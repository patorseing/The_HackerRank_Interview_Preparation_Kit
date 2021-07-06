import unittest
import Solution


class SolveTestCase(unittest.TestCase):
    def testCaseI(self):
        arr = list(map(int, "7 1 3 2 4 5 6".split()))
        actual = Solution.minimumSwaps(arr)
        excepted = 5
        self.assertEqual(actual, excepted)

    def testCaseII(self):
        arr = list(map(int, "4 3 1 2".split()))
        actual = Solution.minimumSwaps(arr)
        excepted = 3
        self.assertEqual(actual, excepted)

    def testCaseIII(self):
        arr = list(map(int, "2 3 4 1 5".split()))
        actual = Solution.minimumSwaps(arr)
        excepted = 3
        self.assertEqual(actual, excepted)

    def testCaseIII(self):
        arr = list(map(int, "1 3 5 2 4 6 7".split()))
        actual = Solution.minimumSwaps(arr)
        excepted = 3
        self.assertEqual(actual, excepted)
