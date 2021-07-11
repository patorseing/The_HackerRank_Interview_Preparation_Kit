import unittest
import Solution


class SolveTestCase(unittest.TestCase):

    def testCaseI(self):
        s = "mom"
        actual = Solution.sherlockAndAnagrams(s)
        excepted = 2
        self.assertEqual(excepted, actual)

    def testCaseII(self):
        s = "abba"
        actual = Solution.sherlockAndAnagrams(s)
        excepted = 4
        self.assertEqual(excepted, actual)

    def testCaseIII(self):
        s = "abcd"
        actual = Solution.sherlockAndAnagrams(s)
        excepted = 0
        self.assertEqual(excepted, actual)

    def testCaseIV(self):
        s = "ifailuhkqq"
        actual = Solution.sherlockAndAnagrams(s)
        excepted = 3
        self.assertEqual(excepted, actual)

    def testCaseV(self):
        s = "kkkk"
        actual = Solution.sherlockAndAnagrams(s)
        excepted = 10
        self.assertEqual(excepted, actual)

    def testCaseVI(self):
        s = "cdcd"
        actual = Solution.sherlockAndAnagrams(s)
        excepted = 5
        self.assertEqual(excepted, actual)

    def testCaseVII(self):
        s = "ifailuhkqqhucpoltgtyovarjsnrbfpvmupwjjjfiwwhrlkpekxxnebfrwibylcvkfealgonjkzwlyfhhkefuvgndgdnbelgruel"
        actual = Solution.sherlockAndAnagrams(s)
        excepted = 399
        self.assertEqual(excepted, actual)

    def testCaseVIII(self):
        s = "gffryqktmwocejbxfidpjfgrrkpowoxwggxaknmltjcpazgtnakcfcogzatyskqjyorcftwxjrtgayvllutrjxpbzggjxbmxpnde"
        actual = Solution.sherlockAndAnagrams(s)
        excepted = 471
        self.assertEqual(excepted, actual)

    def testCaseIX(self):
        s = "mqmtjwxaaaxklheghvqcyhaaegtlyntxmoluqlzvuzgkwhkkfpwarkckansgabfclzgnumdrojexnrdunivxqjzfbzsodycnsnmw"
        actual = Solution.sherlockAndAnagrams(s)
        excepted = 370
        self.assertEqual(excepted, actual)

    def testCaseX(self):
        s = "ofeqjnqnxwidhbuxxhfwargwkikjqwyghpsygjxyrarcoacwnhxyqlrviikfuiuotifznqmzpjrxycnqktkryutpqvbgbgthfges"
        actual = Solution.sherlockAndAnagrams(s)
        excepted = 403
        self.assertEqual(excepted, actual)

    def testCaseX(self):
        s = "zjekimenscyiamnwlpxytkndjsygifmqlqibxxqlauxamfviftquntvkwppxrzuncyenacfivtigvfsadtlytzymuwvpntngkyhw"
        actual = Solution.sherlockAndAnagrams(s)
        excepted = 428
        self.assertEqual(excepted, actual)
