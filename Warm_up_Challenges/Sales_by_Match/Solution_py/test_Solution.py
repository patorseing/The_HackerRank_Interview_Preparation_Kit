import unittest
import Solution

class SolveTestCase(unittest.TestCase):
  def test_caseI(self):
    n = 9
    ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
    actual = Solution.sockMerchant(n, ar)
    excepted = 3
    self.assertEqual(actual, excepted)
