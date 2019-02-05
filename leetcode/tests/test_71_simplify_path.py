import unittest

from leetcode.s71_simplify_path import Solution

class Test71SimplifyPath(unittest.TestCase):
    def setUp(self):
        self.simplify = Solution().simplifyPath

    def test_case1(self):
        ans = self.simplify('/home')
        self.assertEqual(ans, '/home')

    def test_case2(self):
        ans = self.simplify('/')
        self.assertEqual(ans, '/')

    def test_case3(self):
        ans = self.simplify('/home/user')
        self.assertEqual(ans, '/home/user')

    def test_case4(self):
        ans = self.simplify('./home')
        self.assertEqual(ans, '/home')

    def test_case5(self):
        ans = self.simplify('../home')
        self.assertEqual(ans, '/home')

    def test_case6(self):
        ans = self.simplify('/home/../../c')
        self.assertEqual(ans, '/c')

    def test_case7(self):
        ans = self.simplify('/home/')
        self.assertEqual(ans, '/home')

    def test_case8(self):
        ans = self.simplify('/../')
        self.assertEqual(ans, '/')

    def test_case9(self):
        ans = self.simplify('/home//foo')
        self.assertEqual(ans, '/home/foo')

    def test_case10(self):
        ans = self.simplify('/a/./b/../../c/')
        self.assertEqual(ans, '/c')

    def test_case11(self):
        ans = self.simplify('/a/../../b/../c//.//')
        self.assertEqual(ans, '/c')

    def test_case_12(self):
        ans = self.simplify('/a/b///c/d//././/..')
        self.assertEqual(ans, '/a/b/c')

    def test_case_13(self):
        ans = self.simplify('~/git', home='/home/yeukhon')
        self.assertEqual(ans, '/home/yeukhon/git')

    def test_case_14(self):
        ans = self.simplify('~/', home='/home/yeukhon')
        self.assertEqual(ans, '/home/yeukhon')

    def test_case_15(self):
        ans = self.simplify('/tmp/~/.ansible', home='/home/yeukhon')
        self.assertEqual(ans, '/tmp/home/yeukhon/.ansible')

if __name__ == '__main__':
    unittest.main()
