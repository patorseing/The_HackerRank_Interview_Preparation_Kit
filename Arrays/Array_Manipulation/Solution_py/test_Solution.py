import unittest
import Solution


class SolveTestCase(unittest.TestCase):
    def testCaseI(self):
        n = 5
        queries = [[1, 2, 100], [2, 5, 100], [3, 4, 100]]
        actual = Solution.arrayManipulation(n, queries)
        expected = 200
        self.assertEqual(actual, expected)

    def testCaseII(self):
        n = 10
        queries = [[1, 5, 3], [4, 8, 7], [6, 9, 1]]
        actual = Solution.arrayManipulation(n, queries)
        expected = 10
        self.assertEqual(actual, expected)

    def testCaseIII(self):
        n = 10
        queries = [[2, 6, 8], [3, 5, 7], [1, 8, 1], [5, 9, 15]]
        actual = Solution.arrayManipulation(n, queries)
        expected = 31
        self.assertEqual(actual, expected)

    def testCaseIVBig(self):
        with open("../bigtestcase.txt") as file_in:
            readFile = file_in.readlines()
            n = int(readFile[0].rstrip().split()[0])
            queries = []
            for line in readFile[1:]:
                queries.append(list(map(int, line.rstrip().split())))
            actual = Solution.arrayManipulation(n, queries)
            expected = 2497169732
            self.assertEqual(actual, expected)
