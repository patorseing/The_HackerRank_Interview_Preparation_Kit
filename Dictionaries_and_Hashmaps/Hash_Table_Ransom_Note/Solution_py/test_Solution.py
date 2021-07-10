import unittest
import Solution


class SolveTestCase(unittest.TestCase):
    def testCaseI(self):
        m, n = list(map(int, "6 4".rstrip().split()))
        magazine = "give me one grand today night".rstrip().split()
        note = "give one grand today".rstrip().split()
        actual = Solution.checkMagazine(magazine, note)
        excepted = "Yes"
        self.assertEqual(actual, excepted)

    def testCaseII(self):
        m, n = list(map(int, "6 5".rstrip().split()))
        magazine = "two times three is not four".rstrip().split()
        note = "two times two is four".rstrip().split()
        actual = Solution.checkMagazine(magazine, note)
        excepted = "No"
        self.assertEqual(actual, excepted)

    def testCaseIII(self):
        m, n = list(map(int, "7 4".rstrip().split()))
        magazine = "ive got a lovely bunch of coconuts".rstrip().split()
        note = "ive got some coconuts".rstrip().split()
        actual = Solution.checkMagazine(magazine, note)
        excepted = "No"
        self.assertEqual(actual, excepted)

    # count can be note <= mag
    def testCaseIV(self):
        m, n = list(map(int, "15 6".rstrip().split()))
        magazine = "apgo clm w lxkvg mwz elo bg elo lxkvg elo apgo apgo w elo bg".rstrip().split()
        note = "elo lxkvg bg mwz clm w".rstrip().split()
        actual = Solution.checkMagazine(magazine, note)
        excepted = "Yes"
        self.assertEqual(actual, excepted)
