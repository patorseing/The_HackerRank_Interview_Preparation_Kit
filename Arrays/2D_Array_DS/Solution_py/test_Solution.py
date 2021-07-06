import unittest
import Solution

# python -m unittest


class SolveTestCase(unittest.TestCase):

    def test_SolveI(self):
        result = Solution.calHourGlass([[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [
                                       1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]])
        self.assertEqual(result, 19)

    def test_SolveII(self):
        result = Solution.calHourGlass([[-1, -1, 0, -9, -2, -2], [-2, -1, -6, -8, -2, -5], [-1, -1, -
                                                                                            1, -2, -3, -4], [-1, -9, -2, -4, -4, -5], [-7, -3, -3, -2, -9, -9], [-1, -3, -1, -2, -4, -5]])
        self.assertEqual(result, -6)
